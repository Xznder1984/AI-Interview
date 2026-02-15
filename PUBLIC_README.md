# 🎯 AI Mock Interview

**Practice real interviews with AI-powered professional interviewers**

Get live feedback, improve your skills, and ace your next interview.

## ✨ Features

- **5 Interview Personas**: MIT Admissions, Finance Broker, Tech CTO, HR Manager, Management Consultant
- **Real-time AI Responses**: Lifelike interactions that feel like actual interviews
- **Instant Feedback**: Get detailed performance analysis after each interview
- **No Setup Required**: Bring your own OpenRouter API key and start immediately
- **Free to Use**: No backend charges, just use your own API credits
- **Completely Private**: Your data never leaves your browser

## 🚀 Quick Start

### 1. Get an API Key

Visit [OpenRouter.ai](https://openrouter.ai) and:
1. Sign up (free)
2. Go to [Keys](https://openrouter.ai/keys)
3. Create a new API key
4. Copy it (starts with `sk-or-v1-`)

### 2. Start an Interview

1. Visit [AI Mock Interview](https://ai-mock-interview.vercel.app)
2. Paste your API key
3. Select an interview type
4. Answer questions naturally
5. Get feedback at the end

## 📋 Interview Types

| Type | Company | Difficulty | Focus |
|------|---------|-----------|-------|
| MIT Admissions | MIT | Advanced | Intellectual curiosity, problem-solving |
| Finance Broker | Goldman Sachs | Advanced | Market knowledge, deal experience |
| Tech CTO | Startup | Advanced | Technical depth, system design |
| HR Manager | Tech Company | Intermediate | Behavioral, cultural fit |
| Consultant | McKinsey | Advanced | Case studies, analytical thinking |

## 🎓 Tips for Success

1. **Be Specific**: Give detailed examples, not generic answers
2. **Show Your Thinking**: Explain your reasoning and thought process
3. **Ask Questions**: Real candidates ask clarifying questions
4. **Be Authentic**: The AI responds better to genuine answers
5. **Review Feedback**: Read the analysis carefully for improvement areas

## 🔐 Privacy & Security

- Your API key is **stored only in your browser** (sessionStorage)
- Never transmitted to our servers
- You control your own usage and costs
- Interviews are not logged or stored

## 🛠️ Local Development

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-mock-interview.git
cd ai-mock-interview

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "FLASK_SECRET_KEY=your-secret-key" > .env

# Run locally
python src/main.py
```

Visit http://localhost:5000 in your browser.

## 📦 Tech Stack

- **Backend**: Python Flask (lightweight, simple deployment)
- **Frontend**: Vanilla JavaScript (no dependencies)
- **AI**: OpenRouter API (multi-model, reliable)
- **Deployment**: Vercel (fast, serverless)
- **Styling**: Modern CSS (responsive, accessible)

## 📖 Documentation

- **[Deployment Guide](DEPLOYMENT.md)** - Deploy your own version
- **[Local Setup](QUICKSTART.md)** - Run locally for development
- **[OpenRouter Setup](OPENROUTER_SETUP.md)** - API key configuration

## 🐛 Troubleshooting

**"Invalid API key"**
- Check that your key starts with `sk-or-v1-`
- Verify at https://openrouter.ai/keys
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
