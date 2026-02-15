# Quick Start Guide

Get up and running in 5 minutes.

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/Xznder1984/AI-Interview.git
cd AI-Interview
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Get OpenRouter API Key

1. Visit [OpenRouter.ai](https://openrouter.ai)
2. Sign up (free account available)
3. Navigate to "API Keys"
4. Create a new API key
5. Copy the key (starts with `sk-or-v1-`)

### 5. Run Application

```bash
python src/main.py
```

```text
🚀 Starting AI Mock Interview Application...
📍 Server running at http://localhost:5000
```

### 6. Open Your Browser

Visit `http://localhost:5000`

---

## First Interview

1. **Paste API Key** - Enter your OpenRouter key in login form
2. **Select Persona** - Choose from MIT, Finance, Tech, HR, or Case
3. **Read Opening Question** - AI interviewer provides first question
4. **Type Your Response** - Enter your answer in chat box
5. **Press Enter** - Submit your response
6. **Get AI Feedback** - Continue the conversation
7. **End Interview** - Finish when ready
8. **Review Analysis** - See performance feedback

---

## Interview Types

| Type | Focus | Duration |
| --- | --- | --- |
| MIT | College admission | 20-30 min |
| Finance | Banking, investment | 30-45 min |
| Tech | Engineering roles | 45-60 min |
| HR | Behavioral, cultural fit | 25-40 min |
| Case | Consulting, analytics | 45-60 min |

---

## Tips for Success

- Take your time with responses (no time limits)
- Explain your thinking, not just conclusions
- Ask clarifying questions when appropriate
- Be authentic and natural in your responses
- Review feedback after each interview

---

## Troubleshooting

| Issue | Solution |
| --- | --- |
| Module not found | Run `pip install -r requirements.txt` |
| Port 5000 in use | Kill process or change port in `src/main.py` |
| Invalid API key | Verify key format starts with `sk-or-v1-` at openrouter.ai/keys |
| No AI response | Check internet connection, verify OpenRouter account has credits |

---

## Costs

OpenRouter pricing for interviews:

- **GPT-3.5 Turbo**: ~$0.005 per interview
- **GPT-4**: ~$0.03 per interview
- **Free tier**: Includes starter credits

Monitor usage at: [OpenRouter Billing](https://openrouter.ai/account/billing/overview)

---

## Next Steps

- See [README.md](README.md) for complete documentation
- See [API_KEY_GUIDE.md](API_KEY_GUIDE.md) for OpenRouter setup details
- See [DEPLOYMENT.md](DEPLOYMENT.md) for production deployment

---

Ready? Start practicing interviews now! 🎉
