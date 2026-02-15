# Quick Start Guide

Get up and running in 5 minutes.

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/Xznder1984/AI-Interview.git
cd AI-Interview
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Get OpenRouter API Key

1. Visit [OpenRouter.ai](https://openrouter.ai)
2. Sign up (free)
3. Navigate to "Keys"
4. Create new API key
5. Copy key (starts with `sk-or-v1-`)

### 5. Run Application

```bash
python src/main.py
```

You'll see:
```
🚀 Starting AI Mock Interview Application...
📍 Server running at http://localhost:5000
```

### 6. Open Browser

Visit: `http://localhost:5000`

## First Interview

1. **Paste API Key** in login form
2. **Select Persona** (MIT, Finance, Tech, HR, or Case)
3. **Read Opening Question** from AI
4. **Type Your Response** in chat box
5. **Press Enter** to submit
6. **Get AI Feedback** and continue conversation
7. **End Interview** when finished
8. **Review Performance Analysis**

## Tips for Better Interviews

- Take time with your responses (no time limit)
- Explain your thinking, not just conclusions
- Ask clarifying questions if needed
- Be authentic and natural
- Review feedback to improve

## Interview Types

| Type | Focus | Duration |
| --- | --- | --- |
| MIT | College admission | 20-30 min |
| Finance | Banking, investment | 30-45 min |
| Tech | Engineering roles | 45-60 min |
| HR | Behavioral, cultural fit | 25-40 min |
| Case | Consulting, analytics | 45-60 min |

## Troubleshooting

| Issue | Fix |
| --- | --- |
| Module not found | Run `pip install -r requirements.txt` |
| Port 5000 in use | Kill process or change port in src/main.py |
| Invalid API key | Verify key format starts with `sk-or-v1-` |
| No AI response | Check internet, verify OpenRouter credits |

## Costs

OpenRouter pricing:

- **GPT-3.5 Turbo**: ~$0.005 per interview
- **GPT-4**: ~$0.03 per interview
- **Free tier**: Includes starter credits

Check usage: [OpenRouter Billing](https://openrouter.ai/account/billing/overview)

## Full Documentation

See [README.md](README.md) for complete guide and advanced options.

---

**You're ready! Start practicing interviews now! 🎉**
