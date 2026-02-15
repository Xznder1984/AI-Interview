# AI Mock Interview - Developer & Deployment Guide

Complete documentation for understanding, modifying, and deploying the application.

## 📌 Quick Links

- **Users?** → Read [PUBLIC_README.md](PUBLIC_README.md)
- **Get API Key?** → Read [API_KEY_GUIDE.md](API_KEY_GUIDE.md)
- **Deploy to Vercel?** → Read [DEPLOYMENT.md](DEPLOYMENT.md)
- **Quick Setup?** → Read [QUICKSTART.md](QUICKSTART.md)
- **This file** → Detailed developer documentation

## 🎯 Project Overview

AI Mock Interview is a Flask + JavaScript web app that enables users to practice interviews with AI-powered professional interviewers. **Key innovation: users bring their own OpenRouter API keys**, making deployment completely serverless with zero backend secrets.

### Architecture Principles

✅ **No Backend Secrets** - API keys provided by users, never stored  
✅ **Stateless Design** - Each request independent, includes API key  
✅ **Minimal Stack** - Flask + Vanilla JS, easy to understand  
✅ **Privacy First** - User data never leaves their browser  
✅ **Scalable** - Deploys to Vercel with zero databases

## 🚀 Quick Start (5 minutes)

```bash
# 1. Navigate to project
cd "d:\Albarr\VSC-Projects\Python Stuff\ai_phone"

# 2. Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env (optional)
echo "FLASK_SECRET_KEY=dev-secret" > .env

# 5. Run the app
python src/main.py

# 6. Visit http://localhost:5000
# 7. Use a real OpenRouter API key to test
```

## 📚 Documentation Files

| File | Purpose |
|------|---------|
| **README.md** (this file) | Complete developer guide & architecture |
| **PUBLIC_README.md** | For users on GitHub |
| **DEPLOYMENT.md** | Step-by-step Vercel deployment |
| **API_KEY_GUIDE.md** | How to get OpenRouter keys |
| **QUICKSTART.md** | Quick local setup |

## 🏗️ Architecture Overview

### The Problem Solved

Traditional interviewing apps store API keys on servers. This creates:
- Security vulnerability (hacks expose credentials)
- Cost centralization (app pays for all API calls)
- Data privacy concerns (users' data on servers)

### Our Solution

Users provide their own API keys → sent to OpenRouter directly with user's credentials.

```
Browser (User)
    ↓
    └─ Input: "sk-or-v1-..."
    └ Storage: sessionStorage (browser only)
    
    ↓
Flask App (Stateless)
    ↓
    └─ Extract: X-API-Key header
    └─ Validate: Format check (sk-or-v1-*)
    └─ Pass: To InterviewEngine
    └─ Result: Never logged, never stored
    
    ↓
InterviewEngine (Per-User)
    ↓
    └─ Uses: User's API key
    └─ Calls: OpenRouter API
    └─ Returns: Response only
    
    ↓
OpenRouter API
    └─ Authenticates with user's key
    └─ User pays for their usage
    └─ Completely separate accounts
```

## 📁 Project Structure

```
ai_phone/
├── src/
│   ├── main.py                 # Entry point (40 lines)
│   ├── app.py                  # Flask routes (210 lines)
│   └── interview_engine.py      # AI logic (324 lines)
│
├── templates/
│   └── index.html              # Single-page app (300 lines)
│
├── static/
│   ├── script.js               # Frontend logic (400 lines)
│   └── style.css               # Styling (640 lines)
│
├── requirements.txt            # Python deps
├── .env.example                # Environment template
├── .gitignore                  # Git config
├── vercel.json                 # Vercel config
│
└── Documentation/
    ├── README.md               # This file
    ├── PUBLIC_README.md        # For users
    ├── DEPLOYMENT.md           # Deploy instructions
    ├── API_KEY_GUIDE.md        # Getting API keys
    └── QUICKSTART.md           # Quick setup
```

## 💻 Core Components

### src/main.py
**Entry point** - Start Flask server

Key points:
- Does NOT require OPENROUTER_API_KEY in .env
- Does require FLASK_SECRET_KEY (optional, uses default if missing)
- Displays helpful startup message

### src/app.py
**REST API endpoints** - Handle HTTP requests

Key features:
- `@require_api_key` decorator validates X-API-Key header
- Session management (stores engine + API key)
- API key verification on every request
- Clean error responses (401 for bad keys)

Endpoints:
- `GET /` → Serve index.html
- `GET /api/personas` → List interview types
- `POST /api/interview/start` → Begin interview
- `POST /api/interview/respond` → Get AI response
- `POST /api/interview/end` → Get feedback

### src/interview_engine.py
**AI interview logic** - Manage conversations and personas

Key classes:
- `InterviewPersona` - Defines a persona (name, system prompt, etc.)
- `InterviewPersonaLibrary` - 5 pre-configured personas
- `InterviewEngine` - Main orchestration (conversation history, AI calls)

Key methods:
- `get_ai_response(message)` → Call OpenRouter, return response
- `get_interview_feedback()` → Analyze interview, return feedback
- `start_interview(persona_id)` → Initialize, return opening question

### templates/index.html
**User interface** - HTML structure for single-page app

Sections:
- Login form (API key input)
- Persona selection cards
- Chat interface
- Feedback & transcript display

### static/script.js
**Frontend logic** - UI interactions and API calls

Main class:
- `InterviewApp` - Manages state, handles UI, makes API calls

Key method:
- `handleLogin()` → Store API key in sessionStorage
- `sendResponse()` → Send message with X-API-Key header
- All API calls include user's key in header

### static/style.css
**Styling** - Beautiful, responsive design

Features:
- Mobile-first responsive design
- CSS variables for theming
- Smooth animations
- Accessible colors and fonts

## 🔐 Security Deep-Dive

### API Key Flow

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
#   A I - I n t e r v i e w  
 