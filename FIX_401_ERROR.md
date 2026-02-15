## 🔧 Fixing the "401 Unauthorized" Error

### The Problem

You're seeing:
```
Error: API request failed: 401 Client Error: Unauthorized for url 
https://openrouter.ai/api/v1/chat/completions
```

This means the API key is **invalid or doesn't have permission**.

---

## ✅ Step-by-Step Fix

### Step 1: Get a Valid OpenRouter API Key

1. **Visit**: https://openrouter.ai/keys
2. **Sign up or Log in** to your OpenRouter account
3. **Check your account status**:
   - Make sure account is active
   - Make sure you have API credits ($)
4. **Create a new API key** or copy an existing valid one
5. **Copy the full key** (starts with `sk-or-v1-`)

### Step 2: Update Your .env File

Edit `d:\Albarr\VSC-Projects\Python Stuff\ai_phone\.env`:

Replace:
```
OPENROUTER_API_KEY=your-old-key
```

With your **actual** key:
```
OPENROUTER_API_KEY=sk-or-v1-your-actual-key-here
```

⚠️ **Important**:
- No quotes around the key
- No spaces around the `=` sign
- Paste the **full key** from OpenRouter
- Make sure it starts with `sk-or-v1-`

### Step 3: Verify the Key

Before testing, verify your API key:

1. Visit https://openrouter.ai/account/general
2. Check that:
   - ✅ Your account is **active**
   - ✅ You have **API credits**
   - ✅ API key is **created and visible**

### Step 4: Restart the App

Stop and restart the application:

```powershell
# Press CTRL+C in the terminal to stop the server
# Then restart:
python src/main.py
```

### Step 5: Test Again

1. Refresh browser: http://localhost:5000
2. Select an interview type
3. Try to start the interview
4. If it works, you're done! ✅

---

## 🆘 Troubleshooting Guide

### Problem: "Still getting 401 error"

**Check 1: Is your API key valid?**
- Visit https://openrouter.ai/keys
- Copy your API key again
- Make sure you copied the **entire key**
- Paste it exactly in .env (no extra spaces)

**Check 2: Do you have API credits?**
- Visit https://openrouter.ai/account/general
- Check "Balance" or "Credits"
- If $0, add credits to your account
- Free trial might have expired

**Check 3: Is your account active?**
- Visit https://openrouter.ai/account/general
- Make sure account is not suspended
- Check if API access is enabled

**Check 4: Did you restart the app?**
- Stop the server: CTRL+C
- Start again: `python src/main.py`
- Changes to .env require restart

### Problem: "Model not found"

If you get a different error about models, try the default:

In .env, make sure this line is **commented out**:
```
# OPENROUTER_MODEL=openai/gpt-3.5-turbo
```

The app defaults to `gpt-3.5-turbo` which is always available.

### Problem: "Connection timeout"

This means the server can't reach OpenRouter API:

**Check 1: Internet connection**
- Make sure you're connected to internet
- Try opening https://openrouter.ai in browser

**Check 2: Firewall**
- Make sure firewall allows outbound HTTPS
- Try using a different network

**Check 3: OpenRouter status**
- Check https://openrouter.ai/status
- See if service is down

---

## 🔍 How to Verify Your .env File

Your .env file should look like this:

```
# AI Mock Interview Configuration

# OpenRouter API Key (Required)
# Get your API key from: https://openrouter.ai/keys
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxx

# Flask Configuration
FLASK_SECRET_KEY=49d0c2f3d31ef93d59add32bdab5e7be61439869963808703db818ee1f03799
FLASK_ENV=development

# Optional: Model selection
# OPENROUTER_MODEL=openai/gpt-3.5-turbo
```

**Key checks**:
- ✅ `OPENROUTER_API_KEY` has your **real** key
- ✅ Key starts with `sk-or-v1-`
- ✅ No quotes around values
- ✅ No spaces around `=`
- ✅ `FLASK_SECRET_KEY` is present
- ✅ `FLASK_ENV=development`

---

## 📞 Still Having Issues?

If none of the above works:

1. **Create a new OpenRouter account**
   - Visit https://openrouter.ai/
   - Sign up (free)
   - Verify email
   - Add credits if needed

2. **Generate new API key**
   - Visit https://openrouter.ai/keys
   - Click "Create new key"
   - Copy the key
   - Update your .env file

3. **Restart everything**
   - Stop the Flask app (CTRL+C)
   - Close your browser
   - Open fresh terminal
   - Run `python src/main.py`
   - Open http://localhost:5000

---

## ✅ Success Checklist

When the error is fixed, you'll see:
- ✅ Interview page loads
- ✅ "Dr. Sarah Chen" appears as the interviewer
- ✅ Opening question is shown
- ✅ You can type and send responses
- ✅ AI responds with questions
- ✅ Interview timer works

---

## 📚 Need More Help?

See these files:
- `OPENROUTER_SETUP.md` - Complete OpenRouter setup
- `FLASK_SECRET_KEY_GUIDE.md` - Environment variables guide
- `ENV_QUICK_REFERENCE.md` - Quick .env reference

---

**Good luck! You'll get it working! 💪**
