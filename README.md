# Virtual Assistant Project

An intelligent voice and text-based virtual assistant powered by OpenAI's GPT-3.5-turbo, featuring speech recognition, text-to-speech, and various built-in capabilities including weather information, calculations, time queries, and more.

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

## 📋 Prerequisites

### macOS Setup

1. **Install Homebrew** (if not already installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install System Dependencies**:
   ```bash
   brew install portaudio
   brew install python@3.11
   ```

3. **Verify Python Installation**:
   ```bash
   python3.11 --version
   # Should output: Python 3.11.x
   ```

### API Keys Required

1. **OpenAI API Key** (Required):
   - Visit [OpenAI Platform](https://platform.openai.com/)
   - Create an account and generate an API key
   - Note: This is a paid service

2. **Weather API Key** (Optional):
   - Visit [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Generate a free API key

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd virtual_assistant_project
```

### 2. Create Python Virtual Environment
```bash
python3.11 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the project root:
```bash
cp .env.example .env  # If example exists, or create manually
```

Edit `.env` with your configuration:
```env
# OpenAI Configuration (Required)
OPENAI_API_KEY=your_openai_api_key_here

# Assistant Configuration
ASSISTANT_NAME=MyAssistant
ASSISTANT_VOICE_RATE=200
ASSISTANT_VOICE_VOLUME=0.8

# Weather API (Optional)
WEATHER_API_KEY=your_weather_api_key_here

# Development Settings
DEBUG=false
LOG_LEVEL=INFO
```

## 🎮 Usage

### Starting the Assistant
```bash
python src/main.py
```

### Text Mode
- Type your questions or requests
- Use commands like:
  - `"Hello"` - General conversation
  - `"What time is it?"` - Current time
  - `"Weather in Paris"` - Weather information
  - `"Calculate 15 + 27"` - Mathematical operations
  - `"Tell me a joke"` - Entertainment
  - `"voice"` - Switch to voice mode
  - `"quit"`, `"exit"`, `"bye"` - End session

### Voice Mode
- Say `"voice"` in text mode to switch
- Speak naturally after hearing "Listening... (speak now)"
- Wait for response to complete before speaking again
- Use voice commands:
  - `"text mode"` or `"stop listening"` - Switch back to text
  - `"goodbye"` - End session

### Interface Indicators
- `🤖` - Text mode active
- `🎤` - Voice mode active
- `🔊 Speaking...` - TTS in progress
- `🎤 Ready to listen again...` - Ready for voice input
- `Listening... (speak now)` - Actively listening
- `Processing speech...` - Converting speech to text

## 📁 Project Structure

```
virtual_assistant_project/
├── src/
│   ├── main.py              # Application entry point
│   ├── virtual_assistant.py # Core assistant logic
│   └── voice_interface.py   # Speech recognition and TTS
├── config/
│   ├── __init__.py         # Config package marker
│   └── settings.py         # Configuration management
├── tests/                  # Test directory (empty)
├── .env                    # Environment variables (create this)
├── .gitignore             # Git ignore rules
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🔧 Dependencies

### Core Dependencies
- **openai==1.97.1** - OpenAI API client
- **python-dotenv==1.0.0** - Environment variable management
- **requests==2.31.0** - HTTP requests for weather API

### Voice Interface Dependencies
- **speechrecognition==3.14.3** - Speech-to-text conversion
- **pyttsx3==2.90** - Text-to-speech engine
- **pyaudio==0.2.14** - Audio input/output

### macOS Voice Support
- **pyobjc==11.1** - macOS system integration for TTS fallback

### Utility Dependencies
- **schedule==1.2.0** - Task scheduling (future use)

### Optional Dependencies
- **flask==3.0.0** - Web interface framework (not currently used)

## 🔧 Troubleshooting

### Common Issues

#### Voice Mode Not Available
**Symptoms**: "Voice mode is not available" message
**Solutions**:
1. Check microphone permissions:
   ```bash
   # macOS: System Preferences > Security & Privacy > Microphone
   ```
2. Verify PyAudio installation:
   ```bash
   python -c "import pyaudio; print('PyAudio OK')"
   ```
3. Reinstall audio dependencies:
   ```bash
   brew reinstall portaudio
   pip uninstall pyaudio
   pip install pyaudio
   ```

#### pyttsx3 TTS Issues
**Symptoms**: Warning messages about pyttsx3 failing to initialize
**Impact**: The system automatically falls back to macOS system TTS (say command)
**Solutions**:
- This is expected behavior on some macOS systems
- Voice functionality still works using system TTS
- No action required unless you specifically need pyttsx3

#### OpenAI API Errors
**Symptoms**: API authentication or quota errors
**Solutions**:
1. Verify API key in `.env` file
2. Check OpenAI account balance and usage limits
3. Ensure stable internet connection

#### Weather Functionality Issues
**Symptoms**: Weather queries return error messages
**Solutions**:
1. Verify weather API key in `.env` file
2. Check city name spelling
3. Ensure internet connectivity

#### Module Import Errors
**Symptoms**: `ModuleNotFoundError` when running
**Solutions**:
1. Activate virtual environment:
   ```bash
   source .venv/bin/activate
   ```
2. Reinstall dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Performance Optimization

#### Reducing Voice Response Time
- Use faster internet connection for API calls
- Consider using local TTS engines for production use
- Optimize conversation history length

#### Managing Memory Usage
- Restart assistant periodically for long sessions
- Monitor conversation history size
- Consider implementing conversation pruning

## 🔒 Security Considerations

### API Key Management
- Never commit `.env` file to version control
- Use environment variables in production
- Regularly rotate API keys
- Monitor API usage for anomalies

### Network Security
- Use HTTPS for all API calls (handled by libraries)
- Consider API rate limiting in production
- Monitor for excessive API usage

## 🚀 Development

### Adding New Capabilities
1. Add capability function to `VirtualAssistant` class
2. Register in `capabilities` dictionary
3. Add trigger words in `_check_capabilities` method
4. Test with both text and voice modes

### Extending Voice Interface
1. Modify `voice_interface.py` for new TTS engines
2. Add language support in speech recognition
3. Implement custom wake words

### Configuration Options
1. Add new settings to `config/settings.py`
2. Update `.env` file with new variables
3. Document in README

## 📝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly with both text and voice modes
5. Submit a pull request

## 📄 License

This project is for educational purposes. Please respect the terms of service of:
- OpenAI API
- OpenWeatherMap API
- All third-party libraries used

## 🙏 Acknowledgments

- OpenAI for the GPT-3.5-turbo API
- OpenWeatherMap for weather data
- Python speech recognition and TTS library maintainers
- The open-source community for various dependencies

## 📞 Support

For issues and questions:
1. Check this README thoroughly
2. Review error messages and logs
3. Verify all prerequisites are met
4. Check API key configurations

---

**Last Updated**: July 24, 2025
**Version**: 1.0.0
**Python**: 3.11+
**Platform**: macOS (primary), Linux/Windows (compatible)