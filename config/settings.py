import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # API Keys
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
    
    # Assistant Settings
    ASSISTANT_NAME = os.getenv('ASSISTANT_NAME', 'Assistant')
    VOICE_RATE = int(os.getenv('ASSISTANT_VOICE_RATE', 200))
    VOICE_VOLUME = float(os.getenv('ASSISTANT_VOICE_VOLUME', 0.8))
    
    # Voice Recognition Settings
    VOICE_TIMEOUT = int(os.getenv('VOICE_TIMEOUT', 15))  # Time to wait for speech to start
    VOICE_PHRASE_LIMIT = int(os.getenv('VOICE_PHRASE_LIMIT', 15))  # Max phrase length
    VOICE_PAUSE_THRESHOLD = float(os.getenv('VOICE_PAUSE_THRESHOLD', 1.0))  # Silence before phrase end
    
    # Development
    DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    @staticmethod
    def validate():
        """Validate required configuration"""
        if not Config.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is required. Please set it in .env file")
        return True