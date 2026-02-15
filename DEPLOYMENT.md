# Deployment Guide

Deploy AI Mock Interview to Vercel for public access in minutes.

## Prerequisites

- GitHub account ([free signup](https://github.com))
- Vercel account ([free signup](https://vercel.com))
- Git installed locally

## Step 1: Prepare Your Repository

### Initialize Git (if needed)

```bash
cd AI-Interview
git init
git add .
git commit -m "Initial commit: AI Mock Interview app"
```

### Environment Configuration

The `.env` file is in `.gitignore` and will NOT be committed. This is intentional for security.

For local development:
```
FLASK_SECRET_KEY=your-secret-key-here
```

Users won't need `.env` — they provide their OpenRouter API key directly in the web form.

## Step 2: Push to GitHub

### Create GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. Name it `AI-Interview`
3. Skip initializing with README/gitignore (already exist)
4. Copy your repository URL

### Push Your Code

```bash
git remote add origin https://github.com/YOUR_USERNAME/AI-Interview.git
git branch -M main
git push -u origin main
```

## Step 3: Deploy to Vercel

### Connect Repository

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click "New Project"
3. Select "Import Git Repository"
4. Select your `AI-Interview` repository
5. Click "Import"

### Configure Settings

**Framework:** Other (Flask)

**Build Command:** Leave empty

**Output Directory:** Leave empty

**Environment Variables:**
- `FLASK_SECRET_KEY`: Enter a secure value
- Do NOT add `OPENROUTER_API_KEY` (users provide this via form)

### Deploy

Click "Deploy" and wait for build completion.

Your live app: `https://YOUR-PROJECT-NAME.vercel.app`

## Step 4: Share Your App

Your application is now public! Share the link:

```
https://YOUR-PROJECT-NAME.vercel.app
```

Users can:
1. Visit the site
2. Get free OpenRouter API key at [openrouter.ai](https://openrouter.ai)
3. Paste their API key
4. Start interviewing

## Updating Your Deployment

### Make Local Changes

```bash
# Edit files
git add .
git commit -m "Update feature"
git push origin main
```

Vercel automatically rebuilds on each push.

### Update Dependencies

```bash
pip install package_name
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update dependencies"
git push origin main
```

## Troubleshooting

| Problem | Solution |
| --- | --- |
| **Build fails** | Check Vercel build logs, verify requirements.txt |
| **404 errors** | Verify vercel.json routing, check src/main.py exists |
| **API key rejected** | User needs valid OpenRouter key from openrouter.ai |
| **Slow responses** | Check OpenRouter status, verify API credits available |

## Security Best Practices

✅ **What's Secure:**
- Users enter API keys in browser (never sent to backend)
- Keys stored in sessionStorage only
- Each request includes user's own API key
- No backend API key storage

✅ **User Should Know:**
- API key clears when closing browser
- Treat API keys like passwords
- Monitor usage at openrouter.ai
- Revoke keys if compromised

## Custom Domain (Optional)

1. Vercel Dashboard → Settings → Domains
2. Add your custom domain
3. Update DNS records per Vercel instructions

## Support

- [Vercel Docs](https://vercel.com/docs)
- [Flask Deployment](https://flask.palletsprojects.com/deployment/)
- [Report Issues](https://github.com/Xznder1984/AI-Interview/issues)
4. SSL certificate is automatic

## Next Steps

- Monitor usage in Vercel Dashboard
- Consider adding analytics
- Gather user feedback
- Add more interview personas
- Improve AI prompts based on user feedback

## Support

For issues:
1. Check Vercel build logs
2. Review Flask logs in your terminal
3. Test locally with `python src/main.py`
4. Check OpenRouter API status at https://status.openrouter.ai
