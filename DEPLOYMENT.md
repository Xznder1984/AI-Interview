# Deployment Guide: GitHub + Vercel

This guide walks you through deploying AI Mock Interview to GitHub and Vercel for public access.

## Prerequisites

- GitHub account (free at https://github.com)
- Vercel account (free at https://vercel.com)
- Git installed on your computer

## Step 1: Prepare Your Local Repository

### 1.1 Initialize Git (if not already done)

```bash
cd ai_phone
git init
git add .
git commit -m "Initial commit: AI Mock Interview app"
```

### 1.2 Update .env for Production

The `.env` file is in `.gitignore` and will NOT be committed to GitHub. This is intentional for security.

For your local development, you can keep your `.env` file as-is:
```
FLASK_SECRET_KEY=your-secret-key
```

Users won't need a `.env` file - they'll provide their OpenRouter API key directly in the web form.

## Step 2: Push to GitHub

### 2.1 Create a GitHub Repository

1. Go to https://github.com/new
2. Create a repository named `ai-mock-interview`
3. Do NOT initialize with README, .gitignore, or license (we already have these)
4. Copy the repository URL

### 2.2 Add Remote and Push

```bash
git remote add origin https://github.com/YOUR_USERNAME/ai-mock-interview.git
git branch -M main
git push -u origin main
```

## Step 3: Deploy to Vercel

### 3.1 Connect to Vercel

1. Go to https://vercel.com/dashboard
2. Click "New Project"
3. Select "Import Git Repository"
4. Choose your `ai-mock-interview` repository
5. Click "Import"

### 3.2 Configure Project Settings

**Framework Preset:** Other (Flask)

**Build Command:** (Leave empty or use `pip install -r requirements.txt`)

**Output Directory:** Leave empty

**Environment Variables:** 
- Add `FLASK_SECRET_KEY`: Generate a secure value and paste it
- Do NOT add `OPENROUTER_API_KEY` - users provide this via web form

### 3.3 Deploy

Click "Deploy" and wait for the build to complete.

Your app will be available at: `https://ai-mock-interview.vercel.app` (or your custom domain)

## Step 4: Share with Users

Your app is now public! Share the link with others:

```
https://ai-mock-interview.vercel.app
```

Users can:
1. Visit the site
2. Get a free OpenRouter API key at https://openrouter.ai
3. Paste their key into the login form
4. Start practicing interviews

## Updating Your Deployment

### Make Changes Locally
```bash
# Edit files locally
git add .
git commit -m "Describe your changes"
git push origin main
```

Vercel will automatically rebuild and redeploy your changes.

### Update Python Dependencies
If you add new packages:
```bash
pip install new_package
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update dependencies"
git push origin main
```

## Troubleshooting

### Build Fails on Vercel
- Check build logs in Vercel dashboard
- Verify `requirements.txt` has all dependencies
- Ensure `src/main.py` exists and is correct

### App Shows 404 Error
- Verify `vercel.json` routing configuration
- Check that `templates/` and `static/` folders are included

### API Calls Fail with 401
- User has invalid API key format
- User hasn't set up OpenRouter account
- Direct users to https://openrouter.ai/keys

## Security Notes

✅ **Good Security:**
- API key is entered by user in their browser (sessionStorage)
- Never transmitted to our servers
- Each request includes user's own API key
- No backend secrets stored

⚠️ **What Users Should Know:**
- Their API key is stored in browser sessionStorage
- Clearing browser data will clear the key
- The key is never stored on our servers
- They control their own usage/costs

## Custom Domain (Optional)

To use a custom domain with Vercel:

1. In Vercel Dashboard → Settings → Domains
2. Add your domain
3. Update DNS records as instructed
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
