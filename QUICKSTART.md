# ⚡ Quick Start Guide

Get up and running in 5 minutes.

---

## Step 1: Clone Repository

```bash
git clone https://github.com/Xznder1984/AI-Interview.git
cd AI-Interview
```

---

## Step 2: Create Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Get OpenRouter API Key

1. Visit [OpenRouter.ai](https://openrouter.ai)
2. Sign up (free account available)
3. Navigate to "API Keys"
4. Create a new API key
5. Copy the key (starts with `sk-or-v1-`)

---

## Step 5: Run Application

```bash
python src/main.py
```

You'll see:

```
🚀 Starting AI Mock Interview Application...
📍 Server running at http://localhost:5000
```

---

## Step 6: Open Browser

Visit **http://localhost:5000**

---

## Start Your First Interview

1. **Paste API Key** — Enter OpenRouter key
2. **Select Persona** — MIT, Finance, Tech, HR, or Case
3. **Read Opening** — AI provides first question
4. **Type Response** — Enter your answer
5. **Press Enter** — Submit response
6. **Continue Conversation** — Keep practicing
7. **Finish** — End when ready
8. **Review Feedback** — See performance analysis

---

## Interview Types

| Type | Focus | Duration |
| --- | --- | --- |
| **MIT** | College admission | 20-30 min |
| **Finance** | Banking, investment | 30-45 min |
| **Tech** | Engineering roles | 45-60 min |
| **HR** | Behavioral, culture | 25-40 min |
| **Case** | Consulting, analytics | 45-60 min |

---

## Tips for Success

✅ Take your time — no pressure
✅ Explain your thinking — show your process
✅ Ask clarifying questions — natural behavior
✅ Be authentic — genuine answers are best
✅ Review feedback — improve each time

---

## Troubleshooting

| Issue | Solution |
| --- | --- |
| Module not found | Run `pip install -r requirements.txt` |
| Port 5000 in use | Kill process or change port in `src/main.py` |
| Invalid API key | Verify starts with `sk-or-v1-` at [openrouter.ai/keys](https://openrouter.ai/keys) |
| No AI response | Check internet, verify OpenRouter account |

---

## Costs

OpenRouter pricing for interviews:

- **GPT-3.5 Turbo:** ~$0.005 per interview
- **GPT-4:** ~$0.03 per interview
- **Free Tier:** Includes starter credits

Monitor usage: [OpenRouter Billing](https://openrouter.ai/account/billing/overview)

---

## What's Next?

- [Full README](README.md) — Complete documentation
- [API Key Guide](API_KEY_GUIDE.md) — OpenRouter setup details
- [Deployment Guide](DEPLOYMENT.md) — Deploy to production

---

Ready? Start practicing now! 🎉
