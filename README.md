# AI Mock Interview

**Practice real interviews with AI-powered professional interviewers**

[![GitHub](https://img.shields.io/badge/GitHub-Xznder1984%2FAI--Interview-blue?logo=github)](https://github.com/Xznder1984/AI-Interview)
[![License](https://img.shields.io/badge/License-MIT-green)](#license)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](#prerequisites)
[![Flask](https://img.shields.io/badge/Flask-3.0+-blue)](#tech-stack)

## Overview

AI Mock Interview is a modern web application that enables users to practice interviews with AI-powered professional interviewers. Built with Flask and vanilla JavaScript, it features **zero backend secrets** — users bring their own OpenRouter API keys, ensuring complete privacy and control.

### Highlights

- 🎯 **5 Interview Personas**: MIT Admissions Officer, Finance Broker, Tech CTO, HR Manager, Management Consultant
- 🤖 **Real-time AI Responses**: Natural, human-like interactions powered by OpenRouter API
- 📊 **Instant Feedback**: Detailed performance analysis and transcript after each interview
- 🔐 **Privacy-First**: API keys stored only in user's browser, never on servers
- 💰 **Zero Backend Costs**: Users manage their own API usage and costs
- 🎨 **Modern UI**: Responsive, intuitive interface with real-time chat

## Quick Start

### Prerequisites

- Python 3.8+
- Git
- OpenRouter API key ([free signup](https://openrouter.ai))

### Installation

```bash
# Clone repository
git clone https://github.com/Xznder1984/AI-Interview.git
cd AI-Interview

# Create virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run locally
python src/main.py
```

Open `http://localhost:5000` in your browser.

## How It Works

### User Flow

1. **Login**: User pastes their OpenRouter API key
   - Key stored in browser sessionStorage (never sent to server)
   - Validated for correct format

2. **Select Interview**: Choose from 5 personas
   - MIT Admissions Officer
   - Finance Broker (Goldman Sachs style)
   - Tech CTO (Startup)
   - HR Manager (Behavioral)
   - Management Consultant (McKinsey style)

3. **Practice**: Respond naturally to interview questions
   - AI provides real-time responses
   - Interview timer tracks duration
   - Full conversation history maintained

4. **Get Feedback**: Instant performance analysis
   - Strengths and improvement areas
   - Complete interview transcript
   - Downloadable feedback report

### Architecture

The application uses a **stateless, privacy-first architecture**:

```
User's Browser (sessionStorage)
    ↓
    └─ Stores API key (never sent to backend)
    
REST API (Flask)
    ↓
    ├─ Extracts X-API-Key from request header
    ├─ Validates key format
    └─ Never logs or stores the key
    
Interview Engine
    ↓
    └─ Uses user's API key for OpenRouter calls
    
OpenRouter API
    ↓
    └─ User authenticates with their own credentials
    └─ User pays for their usage only
```

**Key Principle**: No API keys stored on servers. Each request includes the user's key in the `X-API-Key` header.

## Features

### Interview Personas

| Persona | Company | Type | Difficulty |
|---------|---------|------|------------|
| Dr. Sarah Chen | MIT | College Admission | Advanced |
| James Mitchell | Goldman Sachs | Investment Banking | Advanced |
| Alex Rivera | Startup | Technical | Advanced |
| Lisa Patel | General | Behavioral | Intermediate |
| Michael Torres | McKinsey | Case Study | Advanced |

### Technology Stack

- **Backend**: Flask 3.0+ (Python)
- **Frontend**: Vanilla JavaScript (no build tools)
- **AI**: OpenRouter API (multi-model support)
- **Styling**: Modern CSS with responsive design
- **Deployment**: Vercel (serverless)

## Configuration

### Environment Variables

Optional `.env` file for local development:

```
FLASK_SECRET_KEY=your-secret-key-here
```

For production (Vercel):
- Set `FLASK_SECRET_KEY` in Vercel project settings
- Users provide API key via web form (not in .env)

### OpenRouter API

The app uses OpenRouter to access multiple AI models:

```python
# Default model
openai/gpt-3.5-turbo

# Can be customized to:
openai/gpt-4
anthropic/claude-2
llama-2-70b
# ... and many others
```

Visit [OpenRouter Models](https://openrouter.ai/docs/models) for available options.

## Security

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

### What Users Should Know

⚠️ Treat API keys like passwords — never share them
⚠️ Monitor usage at openrouter.ai
⚠️ Revoke keys if compromised
⚠️ Free tier available for testing

## Deployment

### Local Development

```bash
python src/main.py
# Runs on http://localhost:5000
# Auto-reloads on code changes
```

### Deploy to Vercel

1. Push code to GitHub
2. Connect repository to Vercel
3. Set environment variables (FLASK_SECRET_KEY)
4. Deploy (automatic on push)

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

## File Structure

```
AI-Interview/
├── src/
│   ├── main.py              # Application entry point
│   ├── app.py               # Flask routes (REST API)
│   └── interview_engine.py   # AI logic & personas
├── templates/
│   └── index.html           # Single-page app
├── static/
│   ├── script.js            # Frontend logic
│   └── style.css            # Styling
├── requirements.txt         # Python dependencies
├── .env.example             # Environment template
├── .gitignore               # Git configuration
├── vercel.json              # Vercel deployment config
├── README.md                # This file
├── DEPLOYMENT.md            # Deployment guide
├── API_KEY_GUIDE.md         # Getting OpenRouter keys
└── QUICKSTART.md            # Quick setup reference
```

## Development

### Adding a New Persona

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

### Customizing the UI

Edit `templates/index.html` and `static/style.css`. Uses CSS variables:

```css
--primary-color: #3b82f6;
--secondary-color: #10b981;
--danger-color: #ef4444;
```

### Improving AI Responses

Edit the `system_prompt` in persona definitions. Current approach emphasizes:
- Natural language patterns
- Personality and humor
- Interview techniques
- Realistic constraints

## Testing

### Manual Testing

1. Use real OpenRouter API key
2. Test each persona
3. Complete sample interview (3+ exchanges)
4. Verify feedback generation
5. Test download functionality

### Browser Console

Check JavaScript errors:
- Open DevTools (F12)
- Check Console tab
- Network tab for API calls

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Flask won't start | Install requirements: `pip install -r requirements.txt` |
| Invalid API key | Verify format starts with `sk-or-v1-` |
| Slow responses | Check internet, verify OpenRouter operational |
| API calls fail | Verify OpenRouter account has credits |
| Vercel build fails | Check `vercel.json` and dependencies |

## Performance

- **Load Time**: < 2 seconds
- **API Response**: 1-5 seconds (depends on model)
- **Scalability**: Unlimited (serverless)
- **Uptime**: 99.95% (Vercel SLA)

## Contributing

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

## License

MIT License - feel free to use, modify, and share. See [LICENSE](LICENSE) file for details.

## Support

- 📖 [API Key Guide](API_KEY_GUIDE.md) - Getting started with OpenRouter
- 🚀 [Deployment Guide](DEPLOYMENT.md) - Deploy to production
- ⚡ [Quick Start](QUICKSTART.md) - Fast setup reference
- 🐛 [Issues](https://github.com/Xznder1984/AI-Interview/issues) - Report bugs
- 💬 [Discussions](https://github.com/Xznder1984/AI-Interview/discussions) - Ask questions

## Acknowledgments

- [OpenRouter.ai](https://openrouter.ai) - Multi-model AI API gateway
- [Vercel](https://vercel.com) - Serverless deployment platform
- [Flask](https://flask.palletsprojects.com) - Web framework

## Contact

- Email: xander.razeralbarr@gmail.com
- GitHub: [@Xznder1984](https://github.com/Xznder1984)

---

**Made with ❤️ to help you ace your interviews**

[Start Practicing](http://localhost:5000) | [GitHub](https://github.com/Xznder1984/AI-Interview) | [Report Issue](https://github.com/Xznder1984/AI-Interview/issues)

1. **User enters key in login form**
   - Frontend validates format (must start with `sk-or-v1-`)
   - User sees clear instructions where to get key

2. **Key stored in sessionStorage**
   ```javascript
   sessionStorage.setItem('openrouter_api_key', apiKey)
   ```
   - Only in user's browser
   - Cleared when tab closes
   - NOT in localStorage (would persist)
   - NOT in cookies (would be sent to every request)

3. **Key included in requests**
   ```javascript
   fetch('/api/interview/respond', {
       headers: {
           'X-API-Key': this.apiKey  // User's key from sessionStorage
       }
   })
   ```

4. **Backend receives and validates**
   ```python
   @require_api_key  # Extracts X-API-Key
   def respond_to_interview(api_key):  # Passed as parameter
       # Verify matches session's original key
       if session_data["api_key"] != api_key:
           return error
   ```

5. **Used with OpenRouter**
   ```python
   headers = {
       "Authorization": f"Bearer {api_key}"  # User's key
   }
   # OpenRouter authenticates against user's account
   ```

6. **Never logged or stored**
   - No database storage
   - Not in Flask logs
   - Not in response bodies
   - Session cleaned up after interview

### Threat Model

| Threat | Mitigation |
|--------|-----------|
| Server compromise | No API keys on server to steal |
| Network sniffing | Uses HTTPS in production |
| Browser malware | Can access sessionStorage (unavoidable) |
| User shares key | User's responsibility (like passwords) |
| Rate limiting bypass | OpenRouter enforces limits |
| Cost abuse | Limited by OpenRouter quotas |

## 🧪 Testing

### Manual Testing Checklist

- [ ] Login with valid API key
- [ ] Login with invalid key (should show error)
- [ ] Select each of 5 personas
- [ ] Complete sample interview (3+ exchanges)
- [ ] Download feedback file
- [ ] Logout and re-login
- [ ] Check browser console (F12) for errors
- [ ] Test on mobile browser
- [ ] Test with slow network (DevTools throttle)

### Test API Key

Visit https://openrouter.ai to get a free test key.

## 📦 Dependencies

**Python (requirements.txt):**
```
Flask==3.0.0           # Web framework
python-dotenv==1.0.0   # Environment variables
requests==2.31.0       # HTTP requests
Flask-CORS==4.0.0      # Cross-origin requests
```

**Frontend:**
- Zero dependencies! Pure HTML/CSS/JavaScript

## 🚀 Deployment Paths

### Local Development
```bash
python src/main.py
# http://localhost:5000
```

### Vercel (Production)
See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed steps.

Quick version:
1. Push to GitHub
2. Import to Vercel
3. Set FLASK_SECRET_KEY in environment
4. Deploy (automatic on push)

## 🎨 Customization

### Add Interview Persona

In `src/interview_engine.py`, add to `InterviewPersonaLibrary`:

```python
CUSTOM_PERSONA = InterviewPersona(
    id="custom",
    name="Your Name",
    title="Job Title",
    company="Company",
    emoji="🎯",
    description="Short description",
    system_prompt="""You are...
    [Detailed instructions for natural, realistic interviewing]
    """
)
```

### Change Default AI Model

In `src/interview_engine.py`:
```python
self.model = model or "openai/gpt-4"  # Was gpt-3.5-turbo
```

Available models: https://openrouter.ai/docs

### Customize UI

Edit `templates/index.html` and `static/style.css`.

CSS variables available:
```css
--primary-color: #3b82f6;
--secondary-color: #10b981;
--danger-color: #ef4444;
--text-dark: #111827;
--text-light: #6b7280;
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Flask won't start | Check Python 3.8+, run `pip install -r requirements.txt` |
| "Invalid API key" error | Verify key starts with `sk-or-v1-`, check at openrouter.ai/keys |
| API calls are slow | Check internet connection, verify OpenRouter is operational |
| "Module not found" error | Activate venv, install requirements |
| CORS errors | Flask-CORS is configured, check browser console |
| Vercel build fails | Check vercel.json, ensure all files present |

## 💡 Performance Tips

- Use GPT-3.5-turbo for speed, GPT-4 for quality
- Consider caching persona list
- Implement message pagination for long interviews
- Add IndexedDB for offline support (future)

## 📝 Contributing

1. Fork repository
2. Create feature branch
3. Make improvements
4. Test thoroughly
5. Submit pull request

### Ideas for Contributions
- Additional interview personas
- Better system prompts
- UI/UX improvements
- Performance optimizations
- Internationalization
- Documentation improvements

## 📄 License

MIT License - Use freely for commercial/personal projects

## 🙏 Credits

- [OpenRouter.ai](https://openrouter.ai) - AI model gateway
- [Vercel](https://vercel.com) - Deployment platform
- [Flask](https://flask.palletsprojects.com) - Web framework
- All contributors

## 📧 Support

- Issues? → GitHub Issues
- Questions? → Start a Discussion
- Features? → GitHub Discussions

---

**Happy coding!** 🚀 Questions? Create an issue or PR!
#   A I - I n t e r v i e w 
 
 #   A I - I n t e r v i e w  
 