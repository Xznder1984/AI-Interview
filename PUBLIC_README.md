# AI Mock Interview

**Practice real interviews with AI-powered professional interviewers**

Get live feedback, improve your skills, and ace your next interview.

## Features

- **5 Interview Personas**: MIT Admissions Officer, Finance Broker, Tech CTO, HR Manager, Management Consultant
- **Real-time AI Responses**: Lifelike interactions that feel like actual interviews
- **Instant Feedback**: Detailed performance analysis after each interview
- **Privacy-First**: Your API key stays in your browser, never on our servers
- **Zero Backend Costs**: Use your own OpenRouter API credits
- **No Sign-up Required**: Bring your own API key and start immediately

## Quick Start

### Step 1: Get an API Key

1. Visit [OpenRouter.ai](https://openrouter.ai)
2. Sign up (free account available)
3. Navigate to [API Keys](https://openrouter.ai/keys)
4. Create a new API key
5. Copy your key (starts with `sk-or-v1-`)

### Step 2: Start an Interview

1. Visit the application
2. Paste your OpenRouter API key
3. Select an interview type
4. Answer questions naturally
5. Get detailed feedback at the end

## Interview Types

| Type | Company Style | Difficulty | Focus Areas |
|------|---------------|-----------|-------------|
| **Admissions** | MIT | Advanced | Intellectual curiosity, problem-solving |
| **Finance** | Goldman Sachs | Advanced | Market knowledge, deal intuition |
| **Technical** | Startup | Advanced | System design, technical depth |
| **Behavioral** | Tech Company | Intermediate | Communication, cultural fit |
| **Case Study** | McKinsey | Advanced | Analytics, business thinking |

## Tips for Success

1. **Be Specific** - Provide detailed examples from real experiences
2. **Show Your Thinking** - Explain your reasoning and approach
3. **Ask Clarifying Questions** - Real interviewees ask questions
4. **Be Authentic** - Genuine answers get better AI feedback
5. **Review Feedback** - Use insights to improve for real interviews

## Privacy & Security

✅ API key stored only in your browser (sessionStorage)
✅ Never sent to or stored on our servers
✅ You control your usage and costs directly
✅ No interview data is logged or retained
✅ Each session is completely isolated

## Local Development

```bash
# Clone repository
git clone https://github.com/Xznder1984/AI-Interview.git
cd AI-Interview

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python src/main.py
```

Visit `http://localhost:5000` in your browser.

## Technology Stack

- **Backend**: Python Flask (lightweight, fast deployment)
- **Frontend**: Vanilla JavaScript (no build tools needed)
- **AI**: OpenRouter API (multi-model access)
- **Deployment**: Vercel (serverless, instant scaling)
- **Styling**: Modern CSS (responsive design)

## Documentation

- [Full README](README.md) - Complete developer documentation
- [Deployment Guide](DEPLOYMENT.md) - Deploy to production
- [API Key Guide](API_KEY_GUIDE.md) - Getting your OpenRouter key
- [Quick Start](QUICKSTART.md) - Fast local setup

## Troubleshooting

**Issue: "Invalid API key"**
- Verify key starts with `sk-or-v1-`
- Check at [OpenRouter Keys](https://openrouter.ai/keys)
- Confirm key is active (not revoked)
- Try creating a new key

**"API request failed"**
- Check your internet connection
- Verify OpenRouter is operational
- Ensure you have credit in your OpenRouter account

**"Interview won't load"**
- Refresh the page
- Clear browser cache
- Try a different interview type

## 💬 Feedback & Improvements

Have ideas? Found a bug? Want to add more personas?

- [Create an issue](https://github.com/yourusername/ai-mock-interview/issues)
- [Submit a PR](https://github.com/yourusername/ai-mock-interview/pulls)
- Email: your-email@example.com

## 📄 License

MIT License - feel free to use, modify, and share

## 🙏 Acknowledgments

- Built with [OpenRouter API](https://openrouter.ai)
- Deployed on [Vercel](https://vercel.com)
- Inspired by real interview experiences

---

**Made with ❤️ to help you succeed in your interviews**

[Start Practicing Now](https://ai-mock-interview.vercel.app) | [GitHub](https://github.com/yourusername/ai-mock-interview) | [Report Issue](https://github.com/yourusername/ai-mock-interview/issues)
