# AI Mock Interview

**Practice real interviews with AI-powered professional interviewers**

[![GitHub](https://img.shields.io/badge/GitHub-Xznder1984%2FAI--Interview-blue?logo=github)](https://github.com/Xznder1984/AI-Interview)
[![License](https://img.shields.io/badge/License-MIT-green)](#license)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](#prerequisites)
[![Flask](https://img.shields.io/badge/Flask-3.0+-blue)](#tech-stack)

---

## 📌 Overview

AI Mock Interview is a modern web application that enables users to practice interviews with AI-powered professional interviewers. Built with **Flask** and **vanilla JavaScript**, it features **zero backend secrets** — users bring their own OpenRouter API keys, ensuring complete privacy and control.

Perfect for job seekers, students, and professionals preparing for:

- College admissions interviews
- Investment banking interviews
- Tech interviews
- Behavioral interviews
- Case study interviews

---

## ✨ Key Features

**🎯 5 Interview Personas**
- MIT Admissions Officer (College Admissions)
- Finance Broker from Goldman Sachs (Investment Banking)
- Tech CTO from Startup (Software Engineering)
- HR Manager (Behavioral)
- McKinsey Senior Consultant (Case Study)

**🤖 Real-time AI Responses**
- Natural, human-like interactions
- Powered by OpenRouter API
- Context-aware follow-up questions

**📊 Instant Feedback**
- Detailed performance analysis
- Complete interview transcript
- Downloadable report

**🔐 Privacy-First Design**
- API keys stored only in user's browser
- Never stored on servers
- No data collection

**💰 Zero Backend Costs**
- Users manage their own API usage
- Pay only for what you use
- Free tier available with OpenRouter

**🎨 Modern, Responsive UI**
- Intuitive interface
- Real-time chat
- Mobile-friendly design

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Git
- OpenRouter API key (free at [openrouter.ai](https://openrouter.ai))

### Installation

```bash
# Clone the repository
git clone https://github.com/Xznder1984/AI-Interview.git
cd AI-Interview

# Create a virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python src/main.py
```

Visit **http://localhost:5000** in your browser to get started.

---

## 💡 How It Works

### User Journey

**1. Login with API Key**
- Paste your OpenRouter API key
- Key is stored securely in your browser (sessionStorage)
- Key is never sent to our servers

**2. Select Interview Type**
Choose from 5 professional interviewers:
- MIT Admissions Officer
- Goldman Sachs Finance Broker
- Tech Startup CTO
- Corporate HR Manager
- McKinsey Management Consultant

**3. Practice Interview**
- Answer realistic interview questions
- Receive real-time AI responses
- Interview timer tracks your performance
- Full conversation history maintained

**4. Review Your Performance**
- Get instant, detailed feedback
- Identify strengths and improvement areas
- Download complete transcript
- Practice as many times as you want

### 🏗️ Architecture

Our application uses a **stateless, privacy-first design**:

```
Your Browser (sessionStorage: API Key)
    ↓
Flask REST API (Receives X-API-Key header)
    ↓
Interview Engine (Uses YOUR API key)
    ↓
OpenRouter API (YOU authenticate with YOUR key)
```

**Core Principle**: Your API key never touches our servers. Each request includes your key in the header for direct authentication.

---

## 🎯 Interview Personas

| Persona | Company | Type | Difficulty |
| --- | --- | --- | --- |
| Dr. Sarah Chen | MIT | College Admission | Advanced |
| James Mitchell | Goldman Sachs | Investment Banking | Advanced |
| Alex Rivera | Startup | Technical | Advanced |
| Lisa Patel | General | Behavioral | Intermediate |
| Michael Torres | McKinsey | Case Study | Advanced |

---

## 🏢 Tech Stack

- **Backend**: Flask 3.0+ (Python)
- **Frontend**: Vanilla JavaScript (no build tools)
- **AI**: OpenRouter API (multi-model support)
- **Styling**: Modern CSS with responsive design
- **Deployment**: Vercel (serverless)

---

## 📁 File Structure

```
AI-Interview/
├── src/
│   ├── main.py                # Application entry point
│   ├── app.py                 # Flask routes (REST API)
│   └── interview_engine.py     # AI logic & personas
├── templates/
│   └── index.html             # Single-page application
├── static/
│   ├── script.js              # Frontend logic
│   └── style.css              # Styling & responsive design
├── requirements.txt           # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore                 # Git configuration
├── vercel.json                # Vercel deployment config
├── README.md                  # This file
├── DEPLOYMENT.md              # Deployment guide
├── API_KEY_GUIDE.md           # Getting OpenRouter API keys
└── QUICKSTART.md              # Quick setup reference
```

---

## 🔐 Security

### API Key Protection

✅ Stored only in user's browser sessionStorage
✅ Never transmitted to our servers
✅ Validated on every request
✅ Cleared when browser is closed
✅ Each session verifies key matches original request

### Data Privacy

✅ No database storage
✅ No session logging
✅ Interview conversations not retained
✅ User data stays in browser

### How It Works

1. User enters API key in login form
2. Frontend validates format (must start with `sk-or-v1-`)
3. Key stored in browser sessionStorage only
4. All API requests include X-API-Key header
5. Backend validates, never stores the key
6. Key used with OpenRouter for AI responses
7. Session cleared when browser closes

### Important for Users

⚠️ Treat API keys like passwords — never share them
⚠️ Monitor usage at openrouter.ai
⚠️ Revoke keys if compromised
⚠️ Use free tier for testing

---

## 🚀 Deployment

### Local Development

```bash
python src/main.py
# Runs on http://localhost:5000
# Auto-reloads on code changes
```

### Deploy to Vercel

1. Push code to GitHub
2. Connect repository to Vercel
3. Set environment variable: `FLASK_SECRET_KEY`
4. Deploy (automatic on push)

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

---

## 🧪 Testing

### Manual Testing Checklist

- Login with valid API key
- Login with invalid key (should show error)
- Select each of 5 personas
- Complete sample interview (3+ exchanges)
- Download feedback file
- Logout and re-login
- Check browser console (F12) for errors
- Test on mobile browser

### Get a Test API Key

Visit https://openrouter.ai to sign up and get a free API key.

---

## 🎨 Customization

### Add New Interview Persona

Edit `src/interview_engine.py`:

```python
NEW_PERSONA = InterviewPersona(
    id="unique-id",
    name="Full Name",
    title="Job Title",
    company="Company Name",
    emoji="🎯",
    description="Short description",
    interview_type="category",
    system_prompt="Detailed instructions for natural interviewing...",
    difficulty_level="advanced",
    focus_areas=["skill1", "skill2"],
    opening_statement="First question to ask..."
)
```

### Change Default AI Model

In `src/interview_engine.py`:

```python
self.model = model or "openai/gpt-4"  # Change from gpt-3.5-turbo
```

Available models: https://openrouter.ai/docs

### Customize UI Theme

Edit CSS variables in `static/style.css`:

```css
--primary-color: #3b82f6;
--secondary-color: #10b981;
--danger-color: #ef4444;
--text-dark: #111827;
--text-light: #6b7280;
```

---

## 🐛 Troubleshooting

| Issue | Solution |
| --- | --- |
| Flask won't start | Install requirements: `pip install -r requirements.txt` |
| Invalid API key error | Verify format starts with `sk-or-v1-` at openrouter.ai/keys |
| Slow API responses | Check internet, verify OpenRouter is operational |
| Module not found error | Activate virtual environment, run `pip install -r requirements.txt` |
| CORS errors | Flask-CORS is configured; check browser console for details |
| Vercel build fails | Check `vercel.json` and ensure all required files present |

---

## 📦 Dependencies

**Python packages (requirements.txt):**
- Flask 3.0.0 - Web framework
- python-dotenv 1.0.0 - Environment variables
- requests 2.31.0 - HTTP requests
- Flask-CORS 4.0.0 - Cross-origin requests

**Frontend:**
- Zero dependencies! Pure HTML/CSS/JavaScript

---

## 📝 Contributing

Contributions welcome! To contribute:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Make improvements
4. Test thoroughly
5. Commit (`git commit -m 'Add amazing feature'`)
6. Push (`git push origin feature/amazing-feature`)
7. Open Pull Request

### Ideas for Contributions

- New interview personas
- Improved AI prompts
- UI/UX enhancements
- Performance optimizations
- Internationalization
- Documentation improvements

---

## 📄 License

MIT License - feel free to use, modify, and share for commercial or personal projects.

---

## 🙏 Credits

- [OpenRouter.ai](https://openrouter.ai) - Multi-model AI API gateway
- [Vercel](https://vercel.com) - Serverless deployment platform
- [Flask](https://flask.palletsprojects.com) - Web framework

---

## 📧 Contact & Support

- 📖 [API Key Guide](API_KEY_GUIDE.md) - Getting started with OpenRouter
- 🚀 [Deployment Guide](DEPLOYMENT.md) - Deploy to production
- ⚡ [Quick Start](QUICKSTART.md) - Fast setup reference
- 🐛 [Issues](https://github.com/Xznder1984/AI-Interview/issues) - Report bugs
- 💬 [Discussions](https://github.com/Xznder1984/AI-Interview/discussions) - Ask questions

---

**Made with ❤️ to help you ace your interviews**

[Start Practicing](http://localhost:5000) | [GitHub Repository](https://github.com/Xznder1984/AI-Interview) | [Report Issue](https://github.com/Xznder1984/AI-Interview/issues)
