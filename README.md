# 🤖 Virtual Assistant Project

A beginner-friendly Python virtual assistant that combines the power of OpenAI's GPT-3.5-turbo with voice recognition and text-to-speech capabilities. Perfect for learning AI integration, Python development, and building interactive applications.

## 🎯 What This Project Does

This virtual assistant can:
- Have natural conversations using AI
- Listen to your voice and respond with speech
- Get real-time weather information for any city
- Perform mathematical calculations
- Tell jokes and provide entertainment
- Switch between text and voice modes seamlessly

## 🌟 Features

### Core Capabilities
- **Conversational AI**: Powered by OpenAI GPT-3.5-turbo for natural language understanding
- **Voice Interface**: Speech-to-text input and text-to-speech output
- **Text Interface**: Traditional keyboard-based interaction
- **Weather Information**: Real-time weather data for any city worldwide
- **Time Queries**: Current date and time information
- **Mathematical Calculations**: Basic arithmetic operations
- **Jokes**: Entertainment with built-in joke collection
- **Reminders**: Simple reminder functionality (basic implementation)

### Interface Modes
- **Text Mode**: Always available, keyboard-based interaction
- **Voice Mode**: Microphone input with spoken responses (when audio hardware is available)
- **Seamless Switching**: Switch between text and voice modes during conversation

### Technical Features
- **Conversation Memory**: Maintains context across multiple exchanges
- **Error Handling**: Graceful fallbacks for failed operations
- **Modular Architecture**: Clean separation of concerns
- **Cross-platform TTS**: Uses pyttsx3 with macOS system TTS fallback
- **Environment Configuration**: Secure API key management via .env files

## 🛠️ System Requirements

### Operating System
- **macOS**: Fully supported (primary development platform)
- **Linux**: Compatible (may require additional audio dependencies)
- **Windows**: Compatible (may require additional audio dependencies)

### Python
- **Python 3.11+** (tested with Python 3.11.9)

### Hardware
- **Microphone**: Required for voice input
- **Speakers/Headphones**: Required for voice output
- **Internet Connection**: Required for OpenAI API and weather data

## 🎓 For Beginners

### What You'll Learn
- Python programming fundamentals
- Working with APIs (OpenAI, Weather)
- Speech recognition and text-to-speech
- Environment variable management
- Project structure and organization
- Error handling and logging

### No Experience? No Problem!
This project is designed to be educational. Each file is well-commented and the code is written to be readable by beginners.

## 📋 Prerequisites & Setup Guide

### Step 1: Install Python
**macOS/Linux:**
```bash
# Install Python 3.11+ using Homebrew (macOS)
brew install python@3.11

# Or download from python.org for other systems
python3 --version  # Should show 3.11+
```

**Windows:**
- Download Python 3.11+ from [python.org](https://python.org)
- Make sure to check "Add Python to PATH" during installation

### Step 2: Get Your API Keys

#### OpenAI API Key (Required)
1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Create an account (you'll get some free credits)
3. Go to API Keys and create a new key
4. Save it - you'll need it later!

#### Weather API Key (Optional but Recommended)
1. Go to [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Generate a free API key
4. Free tier allows 1000 calls/day

### Step 3: System Dependencies (For Voice Features)
**macOS:**
```bash
brew install portaudio
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
```

**Windows:**
Voice features should work out of the box with the Python packages.

## 🚀 Quick Installation Guide

### Method 1: Automatic Setup (Recommended for beginners)
```bash
# 1. Download or clone the project
git clone <repository-url>
cd virtual_assistant_project

# 2. Run the setup script (macOS/Linux)
chmod +x setup.sh
./setup.sh

# 3. Add your API keys (see step 4 below)
```

### Method 2: Manual Setup (Step by step)

#### 1. Download the Project
```bash
git clone <repository-url>
cd virtual_assistant_project
```

#### 2. Create a Virtual Environment
```bash
# Create isolated Python environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate     # macOS/Linux
# OR
.venv\Scripts\activate        # Windows
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Set Up Your API Keys
Create a `.env` file in the project folder:

**Create the file:**
```bash
touch .env  # macOS/Linux
# OR create manually on Windows
```

**Add your keys to `.env`:**
```env
# REQUIRED: Your OpenAI API key
OPENAI_API_KEY=sk-your-actual-openai-key-here

# OPTIONAL: Weather functionality
WEATHER_API_KEY=your-weather-api-key-here

# OPTIONAL: Customize your assistant
ASSISTANT_NAME=MyBot
ASSISTANT_VOICE_RATE=200
ASSISTANT_VOICE_VOLUME=0.8

# OPTIONAL: Debug settings
DEBUG=false
LOG_LEVEL=INFO
```

**⚠️ Important:** Replace `sk-your-actual-openai-key-here` with your real API key from OpenAI!

## 🎮 How to Use Your Assistant

### First Time Running
```bash
# Make sure virtual environment is active
source .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate     # Windows

# Start the assistant
python src/main.py
```

You should see:
```
🚀 Starting Virtual Assistant...
Available modes:
  • Text mode: Always available
  • Voice mode: Available/Not available
🤖 MyBot Text Interface
```

### 💬 Text Mode (Always Available)
Just type and press Enter!

**Try these examples:**
```
You: Hello
MyBot: Hello! How can I help you today?

You: What time is it?
MyBot: The current time is 14:30:25 on 2025-07-24.

You: Weather in Tokyo
MyBot: The weather in Tokyo, JP is 28°C with clear sky.

You: Calculate 25 * 4
MyBot: The result is: 100

You: Tell me a joke
MyBot: Why don't scientists trust atoms? Because they make up everything!

You: voice
MyBot: [Switches to voice mode if available]

You: quit
MyBot: Goodbye! Have a great day!
```

### 🎤 Voice Mode (If Available)
Type `voice` to switch to voice mode. Then:

1. **Wait for the prompt:** "Listening... (you have 15 seconds to start)"
2. **Speak clearly** into your microphone
3. **Wait for the response** - the assistant will speak back to you
4. **Repeat** - it's ready for the next command

**Voice Commands:**
- "What's the weather in London?" 
- "What time is it?"
- "Calculate 50 plus 30"
- "Tell me a joke"
- "Text mode" (switch back to typing)
- "Goodbye" (exit)

### 🔍 Understanding the Interface

**Text Mode Indicators:**
- `🤖 MyBot Text Interface` - You're in text mode
- `You:` - Your turn to type
- `MyBot:` - Assistant's response

**Voice Mode Indicators:**
- `🎤 MyBot Voice Interface` - You're in voice mode  
- `Listening... (speak now)` - Ready for your voice
- `You said: [your words]` - What it heard
- `🔊 Speaking...` - Assistant is talking
- `🎤 Ready to listen again...` - Ready for next command

## 📁 Understanding the Code Structure

```
virtual_assistant_project/
├── src/                     # 🧠 Main application code
│   ├── main.py             # 🚀 Start here - runs the assistant
│   ├── virtual_assistant.py # 🤖 Brain of the assistant (AI logic)
│   └── voice_interface.py  # 🎤 Voice input/output handling
├── config/                 # ⚙️ Settings and configuration
│   ├── __init__.py        # Makes this a Python package
│   └── settings.py        # All settings loaded from .env
├── tests/                 # 🧪 Tests (empty for now)
├── .env                   # 🔐 Your API keys go here (you create this)
├── .gitignore            # 📝 Tells git what files to ignore
├── requirements.txt      # 📦 List of Python packages needed  
├── setup.sh              # 🛠️ Automatic setup script
├── QUICKSTART.md         # ⚡ 5-minute quick start guide
└── README.md            # 📖 This file
```

### 🔍 What Each File Does

**src/main.py (137 lines)**
- The entry point - run this to start your assistant
- Handles switching between text and voice modes
- Manages the main conversation loop
- **Key functions:** `run_text_mode()`, `run_voice_mode()`

**src/virtual_assistant.py (198 lines)**  
- The "brain" - processes what you say and generates responses
- Connects to OpenAI API for conversations
- Has built-in capabilities: weather, time, math, jokes
- **Key functions:** `process_text_input()`, `_generate_ai_response()`

**src/voice_interface.py (144 lines)**
- Handles speech recognition (hearing you speak)  
- Converts text to speech (talking back to you)
- Falls back gracefully if voice hardware isn't available
- **Key functions:** `listen_for_speech()`, `speak()`

**config/settings.py (31 lines)**
- Loads all settings from your .env file
- Validates that required API keys are present
- Sets default values for voice settings
- **Key function:** `Config.validate()`

## 📦 What Packages Are Used & Why

Understanding what each package does helps you learn about Python development:

### 🧠 AI & Core Functionality
- **openai==1.97.1** - Official OpenAI library to talk to ChatGPT API
- **python-dotenv==1.0.0** - Safely loads API keys from .env file
- **requests==2.31.0** - Makes HTTP requests to weather API

### 🎤 Voice Features  
- **speechrecognition==3.14.3** - Converts speech to text (Google Speech API)
- **pyttsx3==2.90** - Converts text to speech (offline TTS engine)
- **pyaudio==0.2.14** - Captures audio from your microphone

### 🖥️ System Integration
- **pyobjc==11.1** - macOS integration (uses built-in `say` command for TTS backup)

### 📅 Future Features
- **schedule==1.2.0** - For scheduling reminders (not used yet, but ready!)

### 🌐 Optional/Future
- **flask==3.0.0** - Web framework (commented out - could add web interface later)

**Total install size:** ~50MB  
**Internet required:** Only for API calls, not for local processing

## 🔧 Troubleshooting for Beginners

### 🚨 Most Common Issues

#### "Voice mode is not available"

**What it means:** Your microphone/audio setup isn't working

**Quick fixes:**
1. **Check microphone permissions:**
   - macOS: System Preferences > Security & Privacy > Microphone
   - Windows: Settings > Privacy > Microphone
   
2. **Test your mic:**
   ```bash
   python -c "import pyaudio; print('PyAudio OK')"
   ```
   
3. **Reinstall audio packages:**
   ```bash
   # macOS
   brew reinstall portaudio
   pip uninstall pyaudio && pip install pyaudio
   
   # Linux
   sudo apt-get install portaudio19-dev
   pip uninstall pyaudio && pip install pyaudio
   ```

#### "ModuleNotFoundError" when running

**What it means:** Python can't find the required packages

**Quick fix:**
```bash
# 1. Make sure virtual environment is active
source .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate     # Windows

# 2. Reinstall packages
pip install -r requirements.txt
```

#### OpenAI API Errors

**Common error messages:**
- "Invalid API key" 
- "You exceeded your current quota"
- "Rate limit exceeded"

**Solutions:**

1. **Check your `.env` file:**
   ```env
   OPENAI_API_KEY=sk-your-actual-key-here  # Make sure this is correct!
   ```

2. **Check your OpenAI account:**
   - Go to [OpenAI Platform](https://platform.openai.com/)
   - Check your usage and billing
   - Make sure you have credits available

3. **Test your API key:**
   ```bash
   python -c "
   import os
   from dotenv import load_dotenv
   load_dotenv()
   print('API Key loaded:', bool(os.getenv('OPENAI_API_KEY')))
   "
   ```

#### Weather Not Working

**Error:** "Sorry, I couldn't find weather information"

**Solutions:**

1. **Add weather API key to `.env`:**
   ```env
   WEATHER_API_KEY=your-weather-key-here
   ```

2. **Try different city formats:**
   - "Weather in Tokyo"
   - "London weather" 
   - "Weather for New York City"

#### TTS Warning Messages (macOS)

**What you see:** "pyttsx3 failed to initialize"

**Don't worry!** This is normal on some Mac systems. The assistant automatically uses the built-in `say` command instead. Voice features still work perfectly.

### 🔧 Advanced Troubleshooting

#### Check if everything is working:
```bash
# Test virtual environment
which python  # Should point to .venv/bin/python

# Test imports
python -c "import openai; print('OpenAI OK')"
python -c "import speech_recognition; print('Speech Recognition OK')"

# Test API connection
python -c "
from src.virtual_assistant import VirtualAssistant
assistant = VirtualAssistant()
print('Assistant initialized successfully!')
"
```

#### Reset everything:
```bash
# Delete virtual environment
rm -rf .venv

# Start fresh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 💡 Performance Tips

#### Making responses faster:
- Use a faster internet connection
- Keep conversation history short
- Consider upgrading OpenAI plan for higher rate limits

#### Managing memory:
- Restart the assistant every few hours for long conversations
- The assistant automatically keeps only the last 20 messages

## 🔒 Security & Best Practices

### 🔐 Keep Your API Keys Safe

**✅ Do this:**
- Keep API keys in `.env` file only
- Never share your `.env` file
- Add `.env` to `.gitignore` (already done)
- Use different keys for development vs production

**❌ Never do this:**
- Put API keys directly in code
- Commit `.env` to git
- Share keys in screenshots or documentation

### 🌐 Network Security
- All API calls use HTTPS automatically
- Monitor your OpenAI usage regularly
- Set up billing alerts in OpenAI dashboard

## 🚀 Learn More: Extending Your Assistant

### 🧩 Adding New Features

Want to add more capabilities? Here's how:

**1. Add a new capability function:**
```python
# In src/virtual_assistant.py, add to the VirtualAssistant class:
def _translate_text(self, query: str) -> str:
    """Translate text using OpenAI"""
    # Your translation logic here
    return "Translation feature"

# Register it in __init__:
self.capabilities['translate'] = self._translate_text
```

**2. Add trigger words:**
```python
# In _check_capabilities method:
elif any(word in user_input_lower for word in ['translate', 'translation']):
    return self.capabilities['translate'](user_input)
```

**3. Test it:**
```bash
You: Translate hello to Spanish
MyBot: Translation feature
```

### 🎤 Customizing Voice Settings

Edit your `.env` file to change voice behavior:
```env
ASSISTANT_VOICE_RATE=150          # Slower speech
ASSISTANT_VOICE_VOLUME=1.0        # Louder volume
VOICE_TIMEOUT=20                  # Wait longer for speech
VOICE_PHRASE_LIMIT=30            # Allow longer phrases
```

### 🌍 Adding More Languages

The speech recognition already supports many languages:
```python
# In voice_interface.py, modify recognize_google call:
text = self.recognizer.recognize_google(audio, language='es-ES')  # Spanish
```

### 🎨 Ideas for Extensions

- **Web interface** (uncomment Flask in requirements.txt)
- **Calendar integration** (Google Calendar API)
- **Smart home control** (IoT device APIs)
- **File management** (create, search, organize files)
- **Note taking** (save conversations to files)
- **Music control** (Spotify API integration)

## 🎓 Learning Resources

### Python Concepts Used
- **Classes and objects** (`VirtualAssistant`, `VoiceInterface`)
- **Error handling** (`try/except` blocks)
- **Environment variables** (`.env` file)
- **API integration** (OpenAI, Weather APIs)
- **Audio processing** (microphone, speakers)

### Next Steps for Learning
1. **Add logging** - Learn about Python logging module
2. **Write tests** - Learn pytest for testing your code
3. **Database integration** - Store conversation history
4. **Web deployment** - Deploy to Heroku or Vercel
5. **Docker** - Containerize the application

## 📄 License & Legal

This project is for **educational purposes only**.

**APIs Used:**
- OpenAI GPT-3.5-turbo (paid service)
- OpenWeatherMap (free tier available)
- Google Speech Recognition (free)

Please respect the terms of service for all APIs and libraries used.

## 🤝 Contributing & Support

### Found a bug or want to contribute?
1. Check existing issues first
2. Create a detailed bug report
3. Fork and create a pull request
4. Test your changes with both text and voice modes

### Need help?
1. Read this README completely
2. Check the QUICKSTART.md for quick solutions  
3. Look at error messages carefully
4. Verify your `.env` file setup
5. Test with simple commands first

---

**🏆 You did it!** You now have a working AI assistant and understand how it works.

**Version**: 1.0.0 | **Python**: 3.11+ | **Last Updated**: July 24, 2025