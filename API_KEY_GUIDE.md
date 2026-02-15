# OpenRouter API Key Guide

## Why Do I Need an API Key?

This application uses OpenRouter API to power realistic AI interviews. OpenRouter is a gateway to multiple AI models.

**You bring your own API key.** Benefits:
- ✅ You control your costs
- ✅ Your data stays in your browser
- ✅ Free tier available for testing
- ✅ No sign-up fees

## Getting Your API Key

### Step 1: Sign Up

Visit [OpenRouter.ai](https://openrouter.ai)

Click "Create Account" and sign up with:
- Email
- Google
- GitHub

**It's free!**

### Step 2: Navigate to Keys

Once logged in:
1. Click your profile icon (top right)
2. Select "Keys"
3. Click "Create Key"
4. Name it "AI Interview Practice"
5. Copy your key

### Step 3: Use Your Key

1. Go to the AI Mock Interview application
2. Paste your key in the login field
3. Click "Login"
4. Start practicing

## API Key Format

Your key should start with:
```
sk-or-v1-...
```

**If it doesn't start with `sk-or-v1-`, you have the wrong key.**

## Troubleshooting

### Invalid API Key

**Check:**
1. Visit [OpenRouter Keys](https://openrouter.ai/keys)
2. Copy the full key without extra spaces
3. Verify it starts with `sk-or-v1-`
4. Ensure the key is not disabled

### Insufficient Credits

You've used your free credits.

**Solution:**
- Check [Billing Overview](https://openrouter.ai/account/billing/overview)
- Free tier includes starter credits
- After using credits, set up a payment method
- Or request additional credits

### Rate Limited

You're sending requests too quickly.

**Solution:**
- Wait a moment and try again
- Check your OpenRouter plan limits
- Consider upgrading for higher limits

## Cost Breakdown

OpenRouter pricing by model:

**Free Tier:**
- Initial free credits included
- Perfect for testing

**Popular Models:**
- GPT-3.5 Turbo: ~$0.001 per 1K tokens
- GPT-4: ~$0.03 per 1K tokens
- Llama 2: Free on free tier
- Claude 2: Variable pricing

**Typical Practice Interview:**
- 10-minute interview: 3,000-5,000 tokens
- GPT-3.5 cost: ~$0.01-$0.05
- Free tier easily covers multiple practice interviews

## Security Tips

- Treat your API key like a password
- Never share it with anyone
- Revoke keys you're not using
- Monitor your usage regularly
- Set spending limits if available

## Support

- [OpenRouter Docs](https://openrouter.ai/docs)
- [Report Issues](https://github.com/Xznder1984/AI-Interview/issues)
- Contact: xander.razeralbarr@gmail.com

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
