"""
Flask Web Application for AI Mock Interview
Provides web interface for conducting interviews and managing sessions
Users provide their own OpenRouter API keys for authentication
"""

import os
from datetime import datetime
from functools import wraps
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from interview_engine import InterviewEngine

app = Flask(__name__, template_folder="../templates", static_folder="../static")
CORS(app)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "your-secret-key-change-in-production")

# Store active interview sessions
interview_sessions = {}


def require_api_key(f):
    """Decorator to require API key from request header"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        
        if not api_key:
            return jsonify({"error": "API key required"}), 401
        
        if not api_key.startswith('sk-or-v1-'):
            return jsonify({"error": "Invalid API key format"}), 401
        
        # Pass API key to the route handler
        return f(*args, api_key=api_key, **kwargs)
    
    return decorated_function


@app.route("/", methods=["GET"])
def index():
    """Render the main page"""
    return render_template("index.html")


@app.route("/api/personas", methods=["GET"])
def get_personas():
    """Get available interview personas (no API key required)"""
    try:
        engine = InterviewEngine(api_key="dummy")  # Don't need real key for this
        personas = engine.get_available_personas()
        return jsonify({"personas": personas})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/interview/start", methods=["POST"])
@require_api_key
def start_interview(api_key):
    """Start a new interview session with user's API key"""
    try:
        data = request.get_json()
        persona_id = data.get("persona_id")
        
        if not persona_id:
            return jsonify({"error": "persona_id not specified"}), 400
        
        # Create new engine with user's API key
        engine = InterviewEngine(api_key=api_key)
        opening_question = engine.start_interview(persona_id)
        
        # Store session with API key
        session_id = f"session_{datetime.now().timestamp()}"
        interview_sessions[session_id] = {
            "engine": engine,
            "api_key": api_key,
            "persona_id": persona_id,
            "start_time": datetime.now().isoformat(),
            "messages": []
        }
        
        return jsonify({
            "session_id": session_id,
            "opening_question": opening_question,
            "persona": {
                "id": engine.current_persona.id,
                "name": engine.current_persona.name,
                "title": engine.current_persona.title,
                "company": engine.current_persona.company
            }
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/interview/respond", methods=["POST"])
@require_api_key
def respond_to_interview(api_key):
    """Send a response during interview and get AI response"""
    try:
        data = request.get_json()
        session_id = data.get("session_id")
        user_message = data.get("user_message")
        
        if not session_id or session_id not in interview_sessions:
            return jsonify({"error": "Invalid session"}), 400
        
        if not user_message:
            return jsonify({"error": "No message provided"}), 400
        
        session_data = interview_sessions[session_id]
        
        # Verify API key matches
        if session_data["api_key"] != api_key:
            return jsonify({"error": "Invalid API key for this session"}), 401
        
        engine = session_data["engine"]
        
        # Get AI response
        ai_response = engine.get_ai_response(user_message)
        
        # Store messages in session
        session_data["messages"].append({
            "role": "user",
            "content": user_message
        })
        session_data["messages"].append({
            "role": "assistant",
            "content": ai_response
        })
        
        return jsonify({
            "response": ai_response
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/interview/end", methods=["POST"])
@require_api_key
def end_interview(api_key):
    """End interview session and get feedback"""
    try:
        data = request.get_json()
        session_id = data.get("session_id")
        
        if not session_id or session_id not in interview_sessions:
            return jsonify({"error": "Invalid session"}), 400
        
        session_data = interview_sessions[session_id]
        
        # Verify API key matches
        if session_data["api_key"] != api_key:
            return jsonify({"error": "Invalid API key for this session"}), 401
        
        engine = session_data["engine"]
        start_time = datetime.fromisoformat(session_data["start_time"])
        duration = (datetime.now() - start_time).total_seconds()
        
        # Get feedback from AI
        feedback = engine.get_interview_feedback()
        
        # Prepare response
        response_data = {
            "duration": f"{int(duration // 60)}m {int(duration % 60)}s",
            "message_count": len(session_data["messages"]) // 2,
            "feedback": feedback
        }
        
        # Clean up session
        del interview_sessions[session_id]
        
        return jsonify(response_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/interview/status", methods=["GET"])
def get_interview_status():
    """Get status of current interview (for health check)"""
    try:
        session_id = request.args.get("session_id")
        
        if not session_id or session_id not in interview_sessions:
            return jsonify({"error": "Invalid session"}), 404
        
        session_data = interview_sessions[session_id]
        
        return jsonify({
            "status": "active",
            "persona_id": session_data["persona_id"],
            "message_count": len(session_data["messages"])
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
