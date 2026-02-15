# 🚀 Quick Start Guide - AI Mock Interview

## 5-Minute Setup

### Step 1: Get Your OpenAI API Key
1. Go to https://platform.openai.com/api-keys
2. Sign up or log in
3. Create a new API key
4. Copy it (you'll need it in a moment)

### Step 2: Configure the Application
1. In the `ai_phone` folder, rename `.env.example` to `.env`
2. Open `.env` in a text editor
3. Paste your API key: `OPENAI_API_KEY=sk-...`
4. Save the file

### Step 3: Install Dependencies
Open PowerShell in the `ai_phone` folder and run:
```powershell
pip install -r requirements.txt
```

### Step 4: Start the Application
```powershell
python src/main.py
```

You should see:
```
🚀 Starting AI Mock Interview Application...
📍 Server running at http://localhost:5000
```

### Step 5: Open Your Browser
Visit: http://localhost:5000

## 🎯 Your First Interview

1. **Choose a Persona**: Click on an interview type
2. **Read the Question**: The AI interviewer will greet you
3. **Type Your Response**: Answer thoughtfully in the text box
4. **Press Enter**: Send your response
5. **Get Feedback**: Read the interviewer's response
6. **Continue**: Have a natural conversation
7. **End Interview**: Click "End Interview" when done
8. **Review Feedback**: Get your performance report

## 💡 Pro Tips

- **Be Thoughtful**: Take time with your answers (no time limit!)
- **Show Your Thinking**: Explain your reasoning, not just the answer
- **Ask Questions**: It's okay to ask clarifying questions
- **Be Natural**: Speak like you would in a real interview
- **Keep Notes**: Review feedback to improve next time

## 🆘 Troubleshooting

**"API key error"**
→ Check your .env file has OPENAI_API_KEY without quotes

**"Port 5000 in use"**
→ Either stop the program using port 5000, or change port in `src/main.py`

**"Module not found"**
→ Run `pip install -r requirements.txt` again

**"No response from AI"**
→ Check internet connection and API key validity

## 📊 Interview Types Explained

| Type | Best For | Duration |
|------|----------|----------|
| MIT Admissions | College prep | 20-30 min |
| Finance Broker | Banking interviews | 30-45 min |
| Tech CTO | Engineering roles | 45-60 min |
| HR Manager | General behavioral | 25-40 min |
| Consultant | Case interviews | 45-60 min |

## 💰 About Costs

OpenAI charges for API usage:
- **GPT-4** (default): ~$0.03 per interview
- **GPT-3.5-turbo** (faster): ~$0.005 per interview

Check your usage at: https://platform.openai.com/account/billing/overview

To use the cheaper model, edit `src/interview_engine.py`:
```python
self.model = "gpt-3.5-turbo"
```

## 📝 Full Documentation

See README.md for complete documentation, features, and advanced setup options.

---

**You're all set! Happy practicing! 🎉**
