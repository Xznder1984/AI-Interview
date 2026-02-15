# 🔐 Flask Secret Key & Environment Setup Guide

## What is a Flask Secret Key?

A Flask secret key is a random string that Flask uses to:
- Encrypt session data
- Secure cookies
- Protect against CSRF attacks
- Sign tokens and data

**It's important to keep it secret and unique!**

---

## 🔑 How to Generate a Secret Key

### Option 1: Using Python (Recommended)

Open Python in your terminal:

```powershell
python
```

Then run:

```python
import secrets
print(secrets.token_hex(32))
```

You'll get something like:
```
a7f8c9d2e3b4f1a6c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0
```

Copy that long string and use it as your `FLASK_SECRET_KEY`.

### Option 2: Using OpenSSL

```powershell
openssl rand -hex 32
```

### Option 3: Quick Python One-Liner

```powershell
python -c "import secrets; print(secrets.token_hex(32))"
```

---

## 📝 Environment Variables Explained

### Required Variables

**OPENROUTER_API_KEY**
```
What: Your OpenRouter API key for AI models
Where to get: https://openrouter.ai/keys
Example: sk-or-v1-1234567890abcdefghijklmnopqrstuvwxyz
```

### Optional but Recommended

**FLASK_SECRET_KEY**
```
What: Secret key for Flask session encryption
How to generate: See above
Example: a7f8c9d2e3b4f1a6c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0
Default: If not set, Flask generates a temporary one (changes on restart)
```

**FLASK_ENV**
```
What: Flask environment mode
Options: 
  - development (debug mode, auto-reload)
  - production (optimized, errors hidden)
Default: development
Example: FLASK_ENV=development
```

**OPENROUTER_MODEL** (Optional)
```
What: Default AI model to use
Options: Any model from https://openrouter.ai/api/v1/models
Default: openai/gpt-3.5-turbo
Example: OPENROUTER_MODEL=anthropic/claude-3-sonnet
```

---

## 📋 Complete .env File Template

```
# Required: OpenRouter API Key
OPENROUTER_API_KEY=sk-or-v1-your-actual-key-here

# Optional: Flask Configuration
FLASK_SECRET_KEY=your-generated-secret-key-here
FLASK_ENV=development

# Optional: AI Model Selection
OPENROUTER_MODEL=openai/gpt-3.5-turbo
```

---

## ✅ Step-by-Step Setup

### Step 1: Generate a Secret Key

Open PowerShell and run:

```powershell
python -c "import secrets; print(secrets.token_hex(32))"
```

**Copy the output** (long hex string).

### Step 2: Get OpenRouter API Key

1. Visit: https://openrouter.ai/keys
2. Sign up if needed
3. Create a new API key
4. Copy it

### Step 3: Create/Edit .env File

In your `ai_phone` folder, create or edit `.env`:

```
OPENROUTER_API_KEY=sk-or-v1-xxxxxx
FLASK_SECRET_KEY=a7f8c9d2e3b4f1a6c8d9e0f1a2b3c4d5e6f7a8b
FLASK_ENV=development
OPENROUTER_MODEL=openai/gpt-3.5-turbo
```

### Step 4: Verify

Make sure your `.env` file:
- ✅ Has `OPENROUTER_API_KEY` with your actual key
- ✅ Has `FLASK_SECRET_KEY` with generated secret
- ✅ Has `FLASK_ENV=development`
- ✅ No quotes around values
- ✅ No spaces around `=`

### Step 5: Run the App

```powershell
python src/main.py
```

If you see "Server running at http://localhost:5000", you're good! ✅

---

## 🔒 Security Tips

✅ **DO:**
- Keep `.env` file secret and never commit to Git
- Use strong, randomly generated secrets
- Change secret key if you think it's compromised
- Use different keys for development and production
- Add `.env` to `.gitignore`

❌ **DON'T:**
- Share your `.env` file
- Commit `.env` to version control
- Use simple/predictable secrets
- Hardcode secrets in code
- Use the same key for multiple projects

---

## 🚀 Example Complete .env

```
# OpenRouter API (Required)
OPENROUTER_API_KEY=sk-or-v1-a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0

# Flask Security (Recommended)
FLASK_SECRET_KEY=7e9f3a2b1c4d6e8f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2

# Flask Mode (Optional, defaults to development)
FLASK_ENV=development

# AI Model (Optional, defaults to gpt-3.5-turbo)
OPENROUTER_MODEL=openai/gpt-3.5-turbo
```

---

## 🆘 Troubleshooting

### "OPENROUTER_API_KEY not found"
- Check `.env` file exists
- Verify spelling of `OPENROUTER_API_KEY`
- Make sure no quotes around the key
- Restart the application

### "InvalidSignatureException" or Cookie Issues
- Your `FLASK_SECRET_KEY` is invalid or missing
- Generate a new one with Python
- Make sure it's a valid hex string

### ".env not being loaded"
- Make sure file is named exactly `.env` (not `.env.txt` or `.env.example`)
- File should be in the root `ai_phone` folder
- Not in `src/` or any subfolder

### "No module named dotenv"
- Run: `pip install python-dotenv`
- Or: `pip install -r requirements.txt`

---

## 📚 Related Files

- `.env.example` - Template for environment variables
- `requirements.txt` - Python package dependencies
- `src/main.py` - Where environment variables are loaded

---

## ✨ You're Ready!

Once you have:
1. ✅ OpenRouter API key
2. ✅ Flask secret key generated
3. ✅ `.env` file with both

You can run: `python src/main.py`

And start using the app! 🎉

---

## 📞 Quick Reference

```
Generate Secret Key:     python -c "import secrets; print(secrets.token_hex(32))"
Get OpenRouter Key:      https://openrouter.ai/keys
Edit .env file:          Your favorite text editor
Run the app:             python src/main.py
Access the app:          http://localhost:5000
```

