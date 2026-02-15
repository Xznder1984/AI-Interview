# 🔑 OpenRouter Setup Guide

## What is OpenRouter?

OpenRouter is an API gateway that provides access to multiple AI models through a single interface. It offers:

- ✅ Access to multiple AI providers (OpenAI, Anthropic, Meta, etc.)
- ✅ Better pricing in many cases
- ✅ Automatic failover between models
- ✅ Simple API compatible with OpenAI format
- ✅ Easy switching between different models
- ✅ Real-time pricing information

## 🚀 Quick Setup

### Step 1: Create OpenRouter Account

1. Go to: https://openrouter.ai/
2. Sign up (free account)
3. Verify your email

### Step 2: Get Your API Key

1. Visit: https://openrouter.ai/keys
2. Create a new key
3. Copy the API key

### Step 3: Add to .env File

```
OPENROUTER_API_KEY=your_api_key_here
```

### Step 4: (Optional) Choose a Model

Edit `.env` file and add your preferred model:

```
OPENROUTER_MODEL=openai/gpt-3.5-turbo
```

## 📊 Recommended Models

### Best Quality (More Expensive)
```
openai/gpt-4-turbo
anthropic/claude-3-opus
```

### Best Balance (Recommended)
```
openai/gpt-3.5-turbo  ← DEFAULT (great quality, cheap)
anthropic/claude-3-sonnet
```

### Cheapest (Still Good Quality)
```
meta-llama/llama-2-70b
mistral/mistral-7b
```

## 💰 Pricing Comparison

OpenRouter often provides better pricing than direct APIs:

| Model | Input (1M tokens) | Output (1M tokens) |
|-------|-------------------|-------------------|
| GPT-3.5-turbo | $0.50 | $1.50 |
| GPT-4 Turbo | $10 | $30 |
| Claude 3 Sonnet | $3 | $15 |
| Llama 2 70B | $0.70 | $0.90 |

Check current pricing: https://openrouter.ai/

## ⚙️ Changing Models

To change the model used in your app:

### Option 1: Edit .env File
```
OPENROUTER_MODEL=anthropic/claude-3-sonnet
```

### Option 2: Edit interview_engine.py
```python
self.model = "anthropic/claude-3-opus"
```

## 🔄 How to Switch Back to OpenAI

If you want to switch back to OpenAI:

1. Install OpenAI package:
   ```
   pip install openai>=1.0.0
   ```

2. Revert the changes to `interview_engine.py` and `requirements.txt`

3. Update `.env.example` with OPENAI_API_KEY

## 🆘 Troubleshooting

### "Unauthorized" Error
- ❌ Wrong API key
- ✅ Check your API key in .env file
- ✅ Make sure no extra spaces or quotes

### "Model not found" Error
- ❌ Model name typo
- ✅ Check model name at: https://openrouter.ai/api/v1/models
- ✅ Use exact model ID from the list

### "Quota exceeded" Error
- ❌ You've hit spending limits
- ✅ Set a monthly budget at: https://openrouter.ai/account/general
- ✅ Top up your account credits

### Slow Responses
- ✅ Try a faster model like gpt-3.5-turbo
- ✅ Check OpenRouter API status
- ✅ Your internet connection

## 📚 Useful Links

- OpenRouter Website: https://openrouter.ai/
- API Keys: https://openrouter.ai/keys
- Models List: https://openrouter.ai/api/v1/models
- API Documentation: https://openrouter.ai/docs
- Account Settings: https://openrouter.ai/account/general

## 🎯 Benefits of OpenRouter

✅ **Flexibility** - Switch models without code changes
✅ **Cost Savings** - Often cheaper than direct APIs
✅ **Reliability** - Automatic failover to backup models
✅ **Simplicity** - Same API format as OpenAI
✅ **Transparency** - Clear pricing and usage tracking
✅ **No Lock-in** - Easy to switch providers

## 📝 Environment Variables Reference

```
# Required
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxx

# Optional
OPENROUTER_MODEL=openai/gpt-3.5-turbo  # Defaults to gpt-3.5-turbo

# Flask config
FLASK_SECRET_KEY=your-secret-key-change-in-production
FLASK_ENV=development
```

## ✅ Verify Setup

To verify your setup works:

1. Make sure .env file has your API key
2. Run: `python src/main.py`
3. Open: http://localhost:5000
4. Start an interview
5. If AI responds, you're all set! ✅

## 🚀 You're Ready!

Your app is now configured to use OpenRouter. Enjoy the flexibility of multiple AI models!

---

**Questions?** Check:
- https://openrouter.ai/docs
- https://openrouter.ai/api/v1/models (see all available models)
