#!/bin/bash

# Virtual Assistant Setup Script for macOS
# Run this script to set up the virtual assistant environment

set -e  # Exit on any error

echo "🚀 Setting up Virtual Assistant..."

# Check if Python 3.11 is available
if ! command -v python3.11 &> /dev/null; then
    echo "❌ Python 3.11 not found. Please install it first:"
    echo "   brew install python@3.11"
    exit 1
fi

# Check if brew is available
if ! command -v brew &> /dev/null; then
    echo "❌ Homebrew not found. Please install it first:"
    echo "   /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
    exit 1
fi

# Install system dependencies
echo "📦 Installing system dependencies..."
brew install portaudio || echo "PortAudio already installed"

# Create virtual environment
echo "🐍 Creating Python virtual environment..."
python3.11 -m venv .venv

# Activate virtual environment
echo "⚡ Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "📈 Upgrading pip..."
pip install --upgrade pip

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please edit .env file and add your API keys:"
    echo "   - OpenAI API Key (required)"
    echo "   - Weather API Key (optional)"
fi

echo "✅ Setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Edit .env file with your API keys"
echo "2. Activate virtual environment: source .venv/bin/activate"
echo "3. Run the assistant: python src/main.py"
echo ""
echo "🎉 Happy chatting with your virtual assistant!"
