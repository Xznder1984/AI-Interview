# Getting Your OpenRouter API Key

## Why Do I Need an API Key?

This app uses the OpenRouter API to power realistic AI interviews. OpenRouter acts as a gateway to multiple AI models, letting us use the best models for natural conversation.

**You provide the API key, not us.** This means:
✅ You control your costs
✅ Your data stays private  
✅ We don't store any of your information
✅ Free tier available

## Step-by-Step Guide

### 1. Go to OpenRouter

Visit **[openrouter.ai](https://openrouter.ai)** in your browser.

### 2. Create an Account

- Click **"Create Account"** (top right)
- Use email, Google, or GitHub to sign up
- **It's completely free!**

### 3. Get Your API Key

Once logged in:

1. Click your profile **icon (top right)**
2. Select **"Keys"** from the dropdown menu
3. Click **"Create Key"**
4. Give it a name like "AI Interview Practice"
5. Copy the key (it starts with `sk-or-v1-`)

### 4. Use Your Key

1. Go to [AI Mock Interview](https://ai-mock-interview.vercel.app)
2. Paste your key into the login box
3. Click **"Start Interviewing"**

## API Key Format

Your key should look like:
```
sk-or-v1-1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6
```

**⚠️ If it doesn't start with `sk-or-v1-`, you have the wrong key!**

## Troubleshooting

### "Invalid API Key"

Check these things:

1. **Is it the right key?**
   - Go to https://openrouter.ai/keys
   - Make sure you copied the full key
   - It should start with `sk-or-v1-`

2. **Did you paste it correctly?**
   - No extra spaces before or after
   - Copy directly from the OpenRouter page

3. **Is the key active?**
   - Check your OpenRouter dashboard
   - Disabled keys won't work

### "Insufficient Credits"

You ran out of free credits. 

- Check your balance at https://openrouter.ai/account/billing/overview
- OpenRouter offers a free tier with initial credits
- After credits run out, you can set up payment

### "Rate Limited"

You're sending requests too fast.

- Wait a moment and try again
- Or check your OpenRouter plan limits

## Cost Information

OpenRouter pricing varies by model:

**Free Tier:** 
- Get initial free credits when you sign up
- Great for testing

**Paid Plans:**
- GPT-3.5 Turbo: ~$0.001 per 1K tokens
- GPT-4: ~$0.03 per 1K tokens
- Other models available too

**For Practice:**
- A typical 10-minute interview uses ~3,000-5,000 tokens
- With GPT-3.5: costs ~$0.01 per interview
- Free tier gives you plenty to practice!

## Security Notes

✅ **Your key is safe with us because:**
- Stored only in your browser (sessionStorage)
- Never sent to our servers
- Never logged or cached anywhere
- Cleared when you close the browser

⚠️ **What you should know:**
- Treat your API key like a password
- Don't share it publicly
- If compromised, regenerate it at openrouter.ai
- Check your bill regularly

## Getting More Credits

1. Go to https://openrouter.ai/account/billing/overview
2. Click "Add Payment Method"
3. Follow the payment instructions
4. Credits are added instantly

## Questions?

- OpenRouter Docs: https://openrouter.ai/docs
- OpenRouter Support: support@openrouter.ai
- Check OpenRouter Status: https://status.openrouter.ai

---

Ready to practice? [Start an Interview](https://ai-mock-interview.vercel.app)
