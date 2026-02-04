# Deploy Ved.digital to Render - Step by Step Guide

## Prerequisites
- GitHub account
- Render account (free tier available at https://render.com)
- Your code pushed to a GitHub repository

## Step 1: Push Your Code to GitHub

1. Initialize git (if not already done):
```bash
git init
git add .
git commit -m "Initial commit - Ready for Render deployment"
```

2. Create a new repository on GitHub:
   - Go to https://github.com/new
   - Name it: `ved-digital` (or any name you prefer)
   - Don't initialize with README (you already have files)
   - Click "Create repository"

3. Push your code:
```bash
git remote add origin https://github.com/YOUR_USERNAME/ved-digital.git
git branch -M main
git push -u origin main
```

## Step 2: Sign Up / Login to Render

1. Go to https://render.com
2. Click "Get Started" or "Sign In"
3. Sign up with GitHub (recommended for easy integration)
4. Authorize Render to access your GitHub repositories

## Step 3: Create a New Web Service

1. From Render Dashboard, click **"New +"** button (top right)
2. Select **"Web Service"**
3. Connect your GitHub repository:
   - If first time: Click "Configure account" to grant Render access
   - Select your `ved-digital` repository
   - Click "Connect"

## Step 4: Configure Your Web Service

Fill in the following settings:

### Basic Settings:
- **Name**: `ved-digital` (or your preferred name)
- **Region**: Choose closest to your target audience (e.g., Oregon, Frankfurt, Singapore)
- **Branch**: `main` (or your default branch)
- **Root Directory**: Leave blank (unless your app is in a subdirectory)

### Build Settings:
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`

### Instance Type:
- **Free** (for testing) or **Starter** ($7/month for better performance)

### Environment Variables (Optional but Recommended):
Click "Add Environment Variable" and add:
- **Key**: `SECRET_KEY`
- **Value**: Generate a random string (e.g., use https://randomkeygen.com/)
- **Key**: `PYTHON_VERSION`
- **Value**: `3.11.0`

## Step 5: Deploy!

1. Click **"Create Web Service"** button at the bottom
2. Render will automatically:
   - Clone your repository
   - Install dependencies from requirements.txt
   - Start your Flask app with Gunicorn
   - Provide you with a live URL

## Step 6: Monitor Deployment

1. Watch the **Logs** tab for deployment progress
2. You'll see:
   - Building...
   - Installing dependencies...
   - Starting server...
   - Live (when successful)

3. Your app will be available at: `https://ved-digital.onrender.com` (or your chosen name)

## Step 7: Verify Deployment

1. Click the URL provided by Render
2. Test all pages:
   - Home page
   - About
   - Services
   - Portfolio
   - Insights
   - Contact form

## Troubleshooting

### If deployment fails:

1. **Check Logs**: Click "Logs" tab to see error messages

2. **Common Issues**:
   - **Module not found**: Make sure all dependencies are in requirements.txt
   - **Port binding error**: Render automatically sets PORT, Gunicorn handles this
   - **Static files not loading**: Check file paths are correct

3. **Redeploy**:
   - Make changes to your code
   - Push to GitHub: `git push`
   - Render auto-deploys on every push (if auto-deploy is enabled)

### Manual Redeploy:
- Go to your service dashboard
- Click "Manual Deploy" → "Deploy latest commit"

## Post-Deployment Tips

### 1. Custom Domain (Optional)
- Go to "Settings" → "Custom Domain"
- Add your domain (e.g., ved.digital)
- Follow DNS configuration instructions

### 2. Enable Auto-Deploy
- Settings → "Auto-Deploy": **Yes**
- Every git push will trigger automatic deployment

### 3. Environment Variables
- Add any secrets in "Environment" tab
- Never commit sensitive data to GitHub

### 4. Monitor Performance
- Check "Metrics" tab for:
  - Response times
  - Memory usage
  - CPU usage

### 5. Free Tier Limitations
- Spins down after 15 minutes of inactivity
- First request after spin-down takes ~30 seconds
- 750 hours/month free
- Upgrade to Starter ($7/month) for always-on service

## Update Your App

To make changes after deployment:

1. Edit your code locally
2. Test locally: `python app.py`
3. Commit changes:
```bash
git add .
git commit -m "Description of changes"
git push
```
4. Render automatically deploys (if auto-deploy enabled)

## Your Deployment Files

I've created these files for you:

- ✅ `requirements.txt` - Updated with gunicorn
- ✅ `render.yaml` - Render configuration (optional, for infrastructure as code)
- ✅ `Procfile` - Process file for deployment
- ✅ `runtime.txt` - Python version specification
- ✅ `app.py` - Updated with environment variable for SECRET_KEY

## Support

- Render Docs: https://render.com/docs
- Render Community: https://community.render.com
- Flask Docs: https://flask.palletsprojects.com/

## Success! 🎉

Your Ved.digital website should now be live on Render!

Share your URL: `https://your-app-name.onrender.com`
