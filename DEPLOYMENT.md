# 🚀 Deployment Guide

Deploy AI Mock Interview to Vercel in minutes.

---

## Prerequisites

- GitHub account ([free signup](https://github.com))
- Vercel account ([free signup](https://vercel.com))
- Git installed locally

---

## Step 1: Prepare Your Repository

### Initialize Git

```bash
cd AI-Interview
git init
git add .
git commit -m "Initial commit: AI Mock Interview app"
```

### Environment Configuration

The `.env` file is in `.gitignore` for security.

For local development, create `.env`:

```bash
FLASK_SECRET_KEY=your-secret-key-here
```

**Important:** Users provide OpenRouter API key via the web form, not in `.env`.

---

## Step 2: Push to GitHub

### Create GitHub Repository

1. Go to [GitHub New Repo](https://github.com/new)
2. Name it `AI-Interview`
3. Skip initializing (README/gitignore exist)
4. Copy the repository URL

### Push Your Code

```bash
git remote add origin https://github.com/YOUR_USERNAME/AI-Interview.git
git branch -M main
git push -u origin main
```

---

## Step 3: Deploy to Vercel

### Connect Repository

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click "New Project"
3. Select "Import Git Repository"
4. Choose your `AI-Interview` repository
5. Click "Import"

### Configure Settings

- **Framework:** Other (Flask)
- **Build Command:** Leave empty
- **Output Directory:** Leave empty

### Set Environment Variables

Add in Vercel project settings:

| Variable | Value |
| --- | --- |
| `FLASK_SECRET_KEY` | Generate secure random string |

**Don't add** `OPENROUTER_API_KEY` — users provide via web form.

### Deploy

Click "Deploy" and wait for build completion.

Your live app: `https://your-project-name.vercel.app`

---

## Step 4: Share Your App

Your application is now public!

Users can:
1. Visit your Vercel URL
2. Get free OpenRouter key at [openrouter.ai](https://openrouter.ai)
3. Paste their API key
4. Start practicing

---

## Update Your Deployment

### Make Code Changes

```bash
# Edit files locally
git add .
git commit -m "Feature: Add new persona"
git push origin main
```

Vercel automatically rebuilds on each push.

### Update Dependencies

```bash
pip install new-package
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update dependencies"
git push origin main
```

---

## Troubleshooting

| Problem | Solution |
| --- | --- |
| Build fails | Check Vercel build logs, verify `requirements.txt` |
| 404 errors | Verify `vercel.json`, ensure `src/main.py` exists |
| API key rejected | User needs valid OpenRouter key from [openrouter.ai/keys](https://openrouter.ai/keys) |
| Slow responses | Check OpenRouter status, verify account has credits |

---

## Security Best Practices

✅ Users enter API keys in browser (never sent to backend)
✅ Keys stored in sessionStorage only (browser memory)
✅ Each request includes user's own API key
✅ No backend stores API keys
✅ Keys cleared when browser closes

⚠️ Users should:
- Treat API keys like passwords
- Never share API keys publicly
- Monitor usage at [OpenRouter Billing](https://openrouter.ai/account/billing/overview)
- Revoke keys if compromised

---

## Custom Domain (Optional)

1. Vercel Dashboard → Settings → Domains
2. Add your custom domain
3. Update DNS records per Vercel instructions
4. SSL certificate is automatic

---

## Performance Monitoring

- Check Vercel Dashboard for deployment history
- View real-time logs for debugging
- Monitor performance metrics
- Track build times

---

## Scaling Considerations

As traffic grows:
- Monitor API usage
- Consider upgrading Vercel plan
- Add analytics/monitoring
- Optimize database queries (if added)

---

## Support & Resources

- [Vercel Documentation](https://vercel.com/docs)
- [Flask Deployment Guide](https://flask.palletsprojects.com/deployment/)
- [OpenRouter API Status](https://status.openrouter.ai)
- [GitHub Issues](https://github.com/Xznder1984/AI-Interview/issues)

---

## Next Steps

- Monitor usage in Vercel Dashboard
- Consider adding analytics
- Gather user feedback
- Add more interview personas
- Refine AI prompts based on real usage
- Prepare for scale as traffic grows

---

# Deployment (Vercel)

1. Push your repository to GitHub.
2. Sign in to Vercel and import the repository.
3. Set the environment variable `FLASK_SECRET_KEY` in Vercel.
4. Deploy — Vercel will build and publish your site.

Notes:
- Do NOT add your OpenRouter API key to Vercel environment variables; users provide it in the app.
- For troubleshooting, check Vercel build logs.

---

Questions? Check the [README](README.md) or [Quick Start](QUICKSTART.md)
