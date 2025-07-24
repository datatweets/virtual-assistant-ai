# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### 1. One-Command Setup (macOS)
```bash
chmod +x setup.sh && ./setup.sh
```

### 2. Add Your API Key
Edit the `.env` file:
```bash
nano .env
# Add your OpenAI API key
```

### 3. Run the Assistant
```bash
source .venv/bin/activate
python src/main.py
```

### 4. Start Chatting!
- Type: `"Hello"`
- Ask: `"What's the weather in Tokyo?"`
- Calculate: `"What's 15 + 27?"`
- Voice mode: `"voice"`
- Exit: `"quit"`

## 🎯 Core Commands

| Command | Description |
|---------|-------------|
| `hello` | Start a conversation |
| `weather in [city]` | Get weather information |
| `what time is it` | Current time |
| `calculate [expression]` | Math operations |
| `tell me a joke` | Random joke |
| `voice` | Switch to voice mode |
| `quit` / `exit` / `bye` | End session |

## 🎤 Voice Mode Commands

| Voice Command | Action |
|---------------|--------|
| "text mode" | Switch back to text |
| "stop listening" | Switch back to text |
| "goodbye" | End session |

## 🔧 Troubleshooting

### Voice Not Working?
```bash
# Check microphone permissions in System Preferences
# Reinstall audio dependencies:
brew reinstall portaudio
pip uninstall pyaudio && pip install pyaudio
```

### TTS Warning Messages?
- pyttsx3 initialization warnings are normal on some macOS systems
- Voice functionality still works using system TTS (say command)
- No action needed - this is expected behavior

### API Errors?
- Check your `.env` file has valid API keys
- Verify internet connection
- Check OpenAI account balance

---
**Need help?** See the full [README.md](README.md) for detailed documentation.
