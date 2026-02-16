# API Key Guide

This app requires users to provide their own OpenRouter API key. The app never stores your key on the server — the key is kept in your browser session and sent with each request.

How it works

- The frontend stores the key in `sessionStorage`.
- The frontend sends the key in the `X-API-Key` header on every request.
- The backend uses the header value for the OpenRouter call and does not persist it.

How to use

1. Open the app in your browser.
2. Paste your OpenRouter API key into the prompt when requested.
3. Start an interview.

Security notes

- Do not paste keys from accounts you cannot revoke.
- The server does not log or save your key.

---

## Troubleshooting

### Invalid API Key Error

**Check:**

- Visit [OpenRouter.ai/keys](https://openrouter.ai/keys)
- Copy entire key without extra spaces
- Verify it starts with `sk-or-v1-`
- Ensure key is enabled (not revoked)

### Insufficient Credits

You've used your free tier credits.

**Solutions:**

- Check [OpenRouter Billing](https://openrouter.ai/account/billing/overview)
- Free tier includes starter credits
- Add payment method for continued usage

### Rate Limited

You're sending requests too quickly (unusual during interviews).

**Solutions:**

- Wait a moment and retry
- Check your OpenRouter plan limits
- Consider upgrading for higher limits

---

## Pricing

OpenRouter pricing by model:

### Free Tier

- Includes starter credits
- Perfect for testing

### Popular Models

| Model | Cost per 1K tokens |
| --- | --- |
| GPT-3.5 Turbo | ~$0.001 |
| GPT-4 | ~$0.03 |
| Claude 2 | Variable |
| Llama 2 | Free |

### Typical Interview Cost

- 10-minute interview: 3,000-5,000 tokens
- GPT-3.5 cost: ~$0.01-$0.05
- Free tier covers multiple interviews

---

## Security & Privacy

### Your Key is Safe Because

✅ Stored only in your browser (sessionStorage)
✅ Never sent to our servers
✅ Never logged or cached anywhere
✅ Automatically cleared when browser closes

### What You Should Know

⚠️ Treat API keys like passwords
⚠️ Never share publicly or on GitHub
⚠️ If compromised, regenerate immediately
⚠️ Monitor usage regularly at [openrouter.ai/account/billing](https://openrouter.ai/account/billing/overview)

---

## Adding Payment Method

1. Go to [OpenRouter Billing](https://openrouter.ai/account/billing/overview)
2. Click "Add Payment Method"
3. Follow payment instructions
4. Credits appear instantly

---

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter API Reference](https://openrouter.ai/docs/api/meta)
- [OpenRouter Status](https://status.openrouter.ai)
- [OpenRouter Support](mailto:support@openrouter.ai)

---

## Next Steps

1. Get your free OpenRouter API key
2. Return to AI Mock Interview app
3. Login with your key
4. Select a persona
5. Practice and improve!

Ready? [Start an Interview](http://localhost:5000)
