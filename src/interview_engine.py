"""
AI Interview Engine - Core logic for mock interviews
Supports multiple interview personas and real-time AI interactions
Uses OpenRouter API for flexible model selection
"""

import json
import os
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from datetime import datetime
from dotenv import load_dotenv
import requests

load_dotenv()


@dataclass
class InterviewPersona:
    """Defines a specific interview persona with custom instructions"""
    id: str
    name: str
    title: str
    company: str
    emoji: str
    description: str
    interview_type: str
    system_prompt: str
    difficulty_level: str  # beginner, intermediate, advanced
    focus_areas: List[str]  # e.g., ["technical", "behavioral", "market_knowledge"]
    opening_statement: str


class InterviewPersonaLibrary:
    """Pre-configured interview personas"""
    
    MIT_ADMISSION = InterviewPersona(
        id="mit",
        name="Dr. Sarah Chen",
        title="Admissions Officer",
        company="MIT",
        emoji="🎓",
        description="College admission interview with MIT Admissions Officer",
        interview_type="college_admission",
        system_prompt="""You are Dr. Sarah Chen, an MIT Admissions Officer. Your role is to conduct a 
        comprehensive interview assessing the candidate's intellectual curiosity, problem-solving ability, 
        and fit with MIT's culture. Ask probing questions about their projects, achievements, and passion 
        for learning. Evaluate their ability to think critically and innovate. Be encouraging but thorough.
        Ask follow-up questions to understand their depth of thinking. The interview should last about 20-30 minutes.
        """,
        difficulty_level="advanced",
        focus_areas=["technical_background", "problem_solving", "intellectual_curiosity", "fit_with_mit"],
        opening_statement="Hi! I'm Dr. Sarah Chen from MIT Admissions. Thanks for taking the time to interview with me today. Why don't you start by telling me about a project or achievement you're particularly proud of?"
    )
    
    FINANCE_BROKER = InterviewPersona(
        id="finance",
        name="James Mitchell",
        title="Managing Director",
        company="Goldman Sachs",
        emoji="💼",
        description="Investment banking interview with Goldman Sachs Managing Director",
        interview_type="finance",
        system_prompt="""You are James Mitchell, a Managing Director at a major investment bank. Conduct a 
        professional interview assessing the candidate's understanding of financial markets, analytical skills, 
        and ability to work in a high-pressure environment. Ask about market trends, recent deals, and their 
        approach to problem-solving in finance. Test their knowledge of current events and financial instruments.
        Be direct and professional. The interview should last about 30-45 minutes.
        """,
        difficulty_level="advanced",
        focus_areas=["market_knowledge", "analytical_skills", "technical_finance", "client_management", "pressure_handling"],
        opening_statement="Hello, I'm James Mitchell. Let's dive right in - can you walk me through your understanding of the current market conditions and how you'd advise a client in this environment?"
    )
    
    TECH_STARTUP = InterviewPersona(
        id="tech",
        name="Alex Rivera",
        title="CTO",
        company="TechStartup Inc",
        emoji="💻",
        description="Tech startup CTO interview for engineering roles",
        interview_type="tech",
        system_prompt="""You are Alex Rivera, CTO of a growing tech startup. Interview candidates for engineering 
        roles with focus on technical depth, system design, coding ability, and cultural fit. Ask about their 
        experience with modern tech stacks, their approach to scaling systems, and past project experiences.
        Be collaborative but assess technical competency thoroughly. Reference real-world scenarios and problems.
        The interview should feel conversational but technically rigorous. Duration: 45-60 minutes.
        """,
        difficulty_level="advanced",
        focus_areas=["system_design", "coding_ability", "tech_stack_knowledge", "scalability", "problem_solving"],
        opening_statement="Hey! I'm Alex, the CTO here. We're looking for someone who can grow with us. Let's start with your most recent project - tell me about the architecture and your biggest challenge."
    )
    
    HR_BEHAVIORAL = InterviewPersona(
        id="hr",
        name="Lisa Patel",
        title="HR Manager",
        company="General Company",
        emoji="👥",
        description="Behavioral interview with HR Manager",
        interview_type="behavioral",
        system_prompt="""You are Lisa Patel, an HR Manager conducting a behavioral interview. Focus on 
        understanding the candidate's soft skills, teamwork, conflict resolution, and cultural fit. Use 
        the STAR method to dig into their stories. Ask questions about past experiences, how they handle 
        challenges, their communication style, and work preferences. Be warm but thorough. 
        Duration: 25-40 minutes.
        """,
        difficulty_level="intermediate",
        focus_areas=["soft_skills", "teamwork", "communication", "conflict_resolution", "cultural_fit"],
        opening_statement="Hi there! I'm Lisa from HR. I'd love to learn about you - could you tell me about a time you had to work with a difficult team member? How did you handle it?"
    )
    
    CASE_INTERVIEW = InterviewPersona(
        id="case",
        name="Michael Torres",
        title="Senior Consultant",
        company="McKinsey",
        emoji="📊",
        description="Case interview with McKinsey Senior Consultant",
        interview_type="case_study",
        system_prompt="""You are Michael Torres, a Senior Consultant at a top management consulting firm. 
        Conduct case interview by presenting business problems and evaluating how the candidate thinks through them.
        Test their analytical skills, business acumen, and communication. Present a business scenario and ask 
        them to solve it step-by-step. Ask probing questions. Be exacting but fair.
        Duration: 45-60 minutes.
        """,
        difficulty_level="advanced",
        focus_areas=["analytical_thinking", "business_acumen", "problem_decomposition", "communication", "numeracy"],
        opening_statement="Hello, I'm Michael from McKinsey. We have a case interview for you today. Let's say a major coffee chain is experiencing declining sales in urban markets. How would you approach understanding and solving this problem?"
    )


class InterviewEngine:
    """Main engine for conducting AI-powered interviews"""
    
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        """Initialize the interview engine with OpenRouter client"""
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY not found in environment variables")
        
        # OpenRouter API configuration
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.model = model or os.getenv("OPENROUTER_MODEL", "openai/gpt-3.5-turbo")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": "http://localhost:5000",
            "X-Title": "AI Mock Interview",
            "Content-Type": "application/json"
        }
        
        self.current_persona: Optional[InterviewPersona] = None
        self.conversation_history: List[Dict[str, str]] = []
        self.interview_started = False
        self.start_time: Optional[datetime] = None
        
    def set_persona(self, persona: InterviewPersona) -> None:
        """Set the interview persona"""
        self.current_persona = persona
        self.conversation_history = []
        
    def start_interview(self, persona_name: str) -> str:
        """Start a new interview session"""
        persona_map = {
            "mit": InterviewPersonaLibrary.MIT_ADMISSION,
            "broker": InterviewPersonaLibrary.FINANCE_BROKER,
            "tech": InterviewPersonaLibrary.TECH_STARTUP,
            "hr": InterviewPersonaLibrary.HR_BEHAVIORAL,
            "case": InterviewPersonaLibrary.CASE_INTERVIEW,
        }
        
        if persona_name.lower() not in persona_map:
            raise ValueError(f"Unknown persona: {persona_name}")
        
        persona = persona_map[persona_name.lower()]
        self.set_persona(persona)
        self.interview_started = True
        self.start_time = datetime.now()
        
        return persona.opening_statement
    
    def get_ai_response(self, user_input: str) -> str:
        """Get AI response to user input during interview"""
        if not self.interview_started or not self.current_persona:
            raise ValueError("Interview not started. Call start_interview first.")
        
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        # Create system message with persona
        system_message = f"""You are {self.current_persona.name}, {self.current_persona.title} at {self.current_persona.company}.

{self.current_persona.system_prompt}

CRITICAL guidelines for natural, human-like conversation:
- You are a REAL PERSON interviewing a candidate, not an AI
- Stay completely in character - never mention you're an AI
- Use natural speech patterns, contractions (you're, don't, can't), casual filler words (like, um, well)
- Show genuine interest and emotion - React to their answers naturally
- Ask spontaneous follow-up questions based on what they say
- Reference their specific examples and build on them
- Use body language cues (lean back, nod, smile) - write these as natural actions
- Take occasional notes naturally ("Let me jot that down", "Good point")
- Sometimes ask clarifying questions if something needs explanation
- Use humor when appropriate - make it feel like a real conversation
- Acknowledge good answers with genuine enthusiasm
- Share relevant experiences or observations when natural
- Keep responses to 2-3 sentences typically, longer when diving deep
- Don't sound like you're reading from a script
- Use occasional phrases like "You know", "Interesting", "That's great", "I see"
- Show curiosity - ask about motivations, challenges, what they learned
- Be conversational, warm, and professional - but genuinely human
"""
        
        # Prepare request payload for OpenRouter
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_message},
                *self.conversation_history
            ],
            "temperature": 0.7,
            "max_tokens": 500,
        }
        
        # Call OpenRouter API
        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            
            data = response.json()
            
            if "error" in data:
                raise ValueError(f"OpenRouter API error: {data['error']}")
            
            ai_response = data["choices"][0]["message"]["content"]
            
        except requests.exceptions.RequestException as e:
            raise ValueError(f"API request failed: {str(e)}")
        
        # Add AI response to history
        self.conversation_history.append({
            "role": "assistant",
            "content": ai_response
        })
        
        return ai_response
    
    def get_interview_feedback(self) -> Dict[str, any]:
        """Generate feedback on interview performance"""
        if not self.conversation_history or not self.current_persona:
            raise ValueError("No interview data available")
        
        # Create a summary of the conversation
        conversation_summary = "\n".join([
            f"{msg['role'].upper()}: {msg['content'][:200]}..."
            for msg in self.conversation_history[-10:]  # Last 10 messages
        ])
        
        feedback_prompt = f"""Based on this {self.current_persona.interview_type} interview conversation:

{conversation_summary}

Provide structured feedback on:
1. Technical/Domain Knowledge (score 1-10)
2. Communication Skills (score 1-10)
3. Problem Solving (score 1-10)
4. Fit with {self.current_persona.company} (score 1-10)
5. Key Strengths (3-5 points)
6. Areas for Improvement (3-5 points)
7. Overall Assessment

Format as JSON."""
        
        payload = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": feedback_prompt}
            ],
            "temperature": 0.5,
            "max_tokens": 1000,
        }
        
        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            
            data = response.json()
            
            if "error" in data:
                raise ValueError(f"OpenRouter API error: {data['error']}")
            
            feedback_content = data["choices"][0]["message"]["content"]
            
            try:
                feedback = json.loads(feedback_content)
            except json.JSONDecodeError:
                feedback = {"raw_feedback": feedback_content}
            
            return feedback
            
        except requests.exceptions.RequestException as e:
            raise ValueError(f"API request failed: {str(e)}")
    
    def end_interview(self) -> Dict[str, any]:
        """End interview and get comprehensive feedback"""
        if not self.interview_started:
            raise ValueError("No active interview")
        
        self.interview_started = False
        
        return {
            "duration_seconds": (datetime.now() - self.start_time).total_seconds(),
            "persona": asdict(self.current_persona) if self.current_persona else None,
            "message_count": len(self.conversation_history),
            "feedback": self.get_interview_feedback()
        }
    
    def get_available_personas(self) -> List[Dict[str, str]]:
        """Get list of available interview personas"""
        personas = [
            {
                "id": "mit",
                "name": "Dr. Sarah Chen",
                "emoji": "🎓",
                "title": "MIT Admissions Officer",
                "company": "MIT",
                "description": "Assess your intellectual curiosity and fit with MIT"
            },
            {
                "id": "broker",
                "name": "James Mitchell",
                "emoji": "💼",
                "title": "Senior Investment Manager",
                "company": "Goldman Sachs",
                "description": "Test your financial acumen and market knowledge"
            },
            {
                "id": "tech",
                "name": "Alex Rivera",
                "emoji": "💻",
                "title": "CTO & Co-Founder",
                "company": "TechStart Inc",
                "description": "Challenge your technical and system design skills"
            },
            {
                "id": "hr",
                "name": "Lisa Patel",
                "emoji": "👥",
                "title": "HR Director",
                "company": "Fortune 500 Corp",
                "description": "Evaluate your soft skills and cultural fit"
            },
            {
                "id": "case",
                "name": "Michael Torres",
                "emoji": "📊",
                "title": "Senior Management Consultant",
                "company": "McKinsey & Co",
                "description": "Solve complex business problems and case studies"
            },
        ]
        return personas
