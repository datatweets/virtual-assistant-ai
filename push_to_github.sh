#!/bin/bash

# GitHub Repository Push Script
# Replace YOUR_USERNAME with your actual GitHub username

echo "🚀 Pushing Virtual Assistant to GitHub..."

# Add remote origin (replace YOUR_USERNAME with your actual username)
echo "Please replace YOUR_USERNAME in the URL below with your actual GitHub username:"
echo "git remote add origin https://github.com/YOUR_USERNAME/virtual-assistant-ai.git"
echo ""
echo "Then run:"
echo "git push -u origin main"
echo ""

# Alternative: If you want to set it up now, uncomment and modify the lines below:
# read -p "Enter your GitHub username: " username
# git remote add origin "https://github.com/$username/virtual-assistant-ai.git"
# git push -u origin main

echo "✅ Setup complete! Your virtual assistant is ready to be pushed to GitHub."