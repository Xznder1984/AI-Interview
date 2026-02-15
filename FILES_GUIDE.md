# 🎯 AI Mock Interview App - Files Guide

## 📖 Where to Start?

**First time here?** → Read `START_HERE.txt` for quick overview

**Want quick setup?** → Follow `QUICKSTART.md` (5 minutes)

**Need full details?** → Read `README.md` (comprehensive)

**Want to understand architecture?** → Read `COMPLETE_OVERVIEW.md`

## 📁 File Directory

### 📄 Documentation Files (Read These)

```
START_HERE.txt
├─ Visual overview of the entire project
├─ Quick start instructions
├─ Example interview conversation
└─ Troubleshooting guide

QUICKSTART.md
├─ 5-minute setup guide
├─ Step-by-step instructions
├─ Pro tips
└─ Interview type reference

README.md
├─ Full documentation
├─ Features list
├─ Installation guide
├─ Configuration options
├─ Troubleshooting
└─ Future enhancements

PROJECT_SUMMARY.md
├─ Complete overview
├─ Feature breakdown
├─ Technology stack
├─ API endpoints
└─ Cost information

COMPLETE_OVERVIEW.md
├─ Detailed architecture
├─ User flow diagrams
├─ API architecture
├─ AI engine explanation
└─ Frontend architecture
```

### 🔧 Configuration Files (Edit These)

```
.env.example
├─ Environment variables template
└─ Copy to .env and add your API key

requirements.txt
├─ Python package dependencies
└─ Used by: pip install -r requirements.txt
```

### 🔧 Setup Scripts (Run These)

```
setup.ps1 (PowerShell - Windows)
├─ Creates virtual environment
├─ Installs dependencies
├─ Sets up configuration
└─ Interactive setup process

setup.bat (Batch - Windows)
├─ Alternative batch file setup
├─ Works with Command Prompt
└─ Same as setup.ps1 in batch form
```

### 🐍 Python Backend (The App)

```
src/
├── main.py
│   ├─ Entry point - START HERE when running app
│   ├─ Validates environment
│   ├─ Displays startup message
│   └─ Starts Flask server
│
├── app.py
│   ├─ Flask web server
│   ├─ REST API endpoints
│   ├─ Session management
│   └─ Request/response handling
│
└── interview_engine.py
    ├─ Core AI interview logic
    ├─ Interview persona definitions
    ├─ OpenAI API integration
    ├─ Conversation management
    └─ Feedback generation
```

### 🌐 Web Interface (The UI)

```
templates/
└── index.html
    ├─ Main HTML page
    ├─ Interview interface structure
    ├─ Welcome/interview/feedback sections
    └─ All content elements

static/
├── style.css
│   ├─ Complete styling
│   ├─ Responsive design
│   ├─ Beautiful animations
│   └─ Mobile-friendly layout
│
└── script.js
    ├─ Frontend JavaScript logic
    ├─ User interactions
    ├─ API communication
    ├─ Real-time chat
    └─ Session management
```

## 🚀 Quick Reference

### To Run the App

```powershell
# First time setup
.\setup.ps1

# Then always
python src/main.py

# Then open
http://localhost:5000
```

### To Add Your API Key

```
1. Open .env file
2. Find: OPENAI_API_KEY=your_openai_api_key_here
3. Replace with actual key: OPENAI_API_KEY=sk-xxx...
4. Save file
5. Restart app
```

### To Change Settings

Edit these lines in files:

**Change AI Model** → `src/interview_engine.py` line 51
```python
self.model = "gpt-3.5-turbo"  # Faster, cheaper
self.model = "gpt-4"  # More powerful
```

**Change Port** → `src/main.py` last line
```python
app.run(debug=True, host="0.0.0.0", port=5001)  # Change 5001
```

**Add New Persona** → `src/interview_engine.py` class `InterviewPersonaLibrary`
```python
NEW_PERSONA = InterviewPersona(
    name="Your Name",
    ...
)
```

### To Customize UI

**Change Colors** → Edit `static/style.css` starting at `:root`

**Change Layout** → Edit `templates/index.html` sections

**Change Behavior** → Edit `static/script.js` class `InterviewApp`

## 📊 File Sizes (Approximate)

| File | Size | Purpose |
|------|------|---------|
| main.py | 1 KB | Entry point |
| app.py | 6 KB | Flask server |
| interview_engine.py | 12 KB | AI logic |
| index.html | 5 KB | Web structure |
| style.css | 8 KB | Web styling |
| script.js | 9 KB | Web logic |
| requirements.txt | 1 KB | Dependencies |

**Total Code: ~40 KB** (Very lightweight!)

## 🔄 Development Workflow

### Make Changes to AI Behavior
→ Edit `src/interview_engine.py`
→ Restart `python src/main.py`

### Make Changes to Web UI
→ Edit `templates/index.html` or `static/style.css`
→ Refresh browser (no restart needed)

### Make Changes to Frontend Logic
→ Edit `static/script.js`
→ Refresh browser (no restart needed)

### Make Changes to Web Server
→ Edit `src/app.py`
→ Restart `python src/main.py`

## 🎓 Learning Path

### Beginner
1. Read `START_HERE.txt`
2. Run `setup.ps1`
3. Start interviewing
4. Review feedback

### Intermediate
1. Read `QUICKSTART.md`
2. Explore the files
3. Try different personas
4. Track your improvement

### Advanced
1. Read `COMPLETE_OVERVIEW.md`
2. Study the architecture
3. Add custom personas
4. Modify the AI behavior
5. Customize the UI

## 🆘 File-Specific Help

### Having Issues with...

**Setup?**
→ Read: `QUICKSTART.md`
→ Check: `.env.example` and `.env`
→ Try: `setup.ps1` or `setup.bat`

**Running the app?**
→ Read: `README.md`
→ Check: `src/main.py`
→ Verify: API key in `.env`

**Using the web interface?**
→ Read: `START_HERE.txt`
→ Check: `templates/index.html`
→ Try: Refresh browser

**AI responses?**
→ Read: `COMPLETE_OVERVIEW.md`
→ Check: `src/interview_engine.py`
→ Verify: API key and quota

**Customizing?**
→ Read: `README.md` (Customization section)
→ Edit: Specific files mentioned

## 📈 File Dependencies

```
main.py
  └─ imports: app.py
      └─ imports: interview_engine.py
          └─ imports: openai

index.html
  └─ links: style.css
  └─ links: script.js
      └─ calls: app.py REST endpoints
```

## 💾 Backup Important Files

Keep backups of:
- `.env` (contains your API key!)
- `src/interview_engine.py` (if you customize)
- Any custom personas you create

## 🔐 Security Notes

**Files with sensitive data:**
- `.env` - Contains API key, don't share!
- `.env` - Add to `.gitignore` if using git

**Safe to edit:**
- All `.py` files
- All `.js` files
- All `.css` files
- `*.md` files

**Don't delete:**
- `requirements.txt` (needed for setup)
- `templates/index.html` (needed for UI)
- `static/` folder (needed for styling)

## 🎯 Next Steps

1. **New User?** → Open `START_HERE.txt`
2. **Quick Setup?** → Run `setup.ps1`
3. **Full Docs?** → Read `README.md`
4. **Want Details?** → Read `COMPLETE_OVERVIEW.md`
5. **Ready to Go?** → Run `python src/main.py`

---

**All files are included and ready to use!** 🚀
