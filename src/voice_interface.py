import logging
import subprocess
import platform
import time
from typing import Optional

from config.settings import Config

logger = logging.getLogger(__name__)

# Initialize voice availability flag
VOICE_AVAILABLE = False

try:
    import speech_recognition as sr
    VOICE_AVAILABLE = True
    logger.info("Speech recognition library loaded successfully")
except ImportError:
    logger.warning("Speech recognition not installed. Install speech-recognition for voice features.")
except Exception as e:
    logger.warning(f"Speech recognition available but failed to initialize: {e}")

# Try to import pyttsx3, but don't make it required
TTS_AVAILABLE = False
try:
    import pyttsx3
    TTS_AVAILABLE = True
    logger.info("pyttsx3 TTS library loaded successfully")
except ImportError:
    logger.info("pyttsx3 not available, will use system TTS")
except Exception as e:
    logger.warning(f"pyttsx3 available but failed to load: {e}")

class VoiceInterface:
    def __init__(self):
        self.available = VOICE_AVAILABLE
        self.tts_engine = None
        self.use_system_tts = False
        
        if not self.available:
            logger.warning("Voice libraries not available. Install speech_recognition for voice features.")
            return
        
        try:
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
            
            # Try to initialize pyttsx3 TTS
            if TTS_AVAILABLE:
                try:
                    self.tts_engine = pyttsx3.init()
                    self.tts_engine.setProperty('rate', Config.VOICE_RATE)
                    self.tts_engine.setProperty('volume', Config.VOICE_VOLUME)
                    logger.info("pyttsx3 TTS engine initialized successfully")
                except Exception as e:
                    logger.info(f"pyttsx3 TTS failed to initialize, using system TTS: {e}")
                    self.tts_engine = None
                    self.use_system_tts = True
            else:
                self.use_system_tts = True
            
            if self.use_system_tts and platform.system() == "Darwin":
                logger.info("Using macOS system TTS (say command)")
            
            # Calibrate for ambient noise and adjust settings
            with self.microphone as source:
                logger.info("Calibrating for ambient noise...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
            
            # Adjust recognition settings for better speech capture
            self.recognizer.pause_threshold = Config.VOICE_PAUSE_THRESHOLD  # Seconds of silence before considering phrase complete
            self.recognizer.energy_threshold = 300  # Minimum audio energy to consider for recording
            self.recognizer.dynamic_energy_threshold = True  # Automatically adjust energy threshold
            
            logger.info("Voice interface initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize voice interface: {e}")
            # Set instance flag to indicate voice is not available
            self.available = False
    
    def listen_for_speech(self, timeout: int = None) -> Optional[str]:
        """Listen for speech input with improved timing"""
        if not self.available:
            return None
        
        # Use config values or provided timeout
        actual_timeout = timeout or Config.VOICE_TIMEOUT
        phrase_limit = Config.VOICE_PHRASE_LIMIT
            
        try:
            print(f"Listening... (you have {actual_timeout} seconds to start and {phrase_limit} seconds total)")
            with self.microphone as source:
                # Listen with generous timeout and phrase length
                # timeout: time to wait for speech to start
                # phrase_time_limit: maximum length of phrase
                audio = self.recognizer.listen(
                    source, 
                    timeout=actual_timeout,        # Configurable time to start speaking
                    phrase_time_limit=phrase_limit # Configurable total phrase length
                )
            
            print("Processing speech...")
            # Use Google's speech recognition
            text = self.recognizer.recognize_google(audio)
            logger.info(f"Recognized speech: {text}")
            return text
            
        except sr.WaitTimeoutError:
            print("No speech detected within timeout")
            return None
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said")
            return None
        except sr.RequestError as e:
            logger.error(f"Speech recognition error: {e}")
            print("Sorry, there was an error with the speech recognition service")
            return None
    
    def speak(self, text: str):
        """Convert text to speech"""
        if not self.available:
            print(f"Assistant: {text}")
            return
            
        try:
            if self.tts_engine:
                # Use pyttsx3 TTS (synchronous)
                self.tts_engine.say(text)
                self.tts_engine.runAndWait()
                
            elif self.use_system_tts and platform.system() == "Darwin":
                # Use macOS built-in say command (synchronous)
                subprocess.run(['say', text], check=False)
                
            else:
                # Fallback to text output
                print(f"Assistant: {text}")
            
            # Small delay to ensure TTS is completely finished
            time.sleep(0.5)
            
        except Exception as e:
            logger.error(f"TTS error: {e}")
            print(f"Assistant: {text}")  # Fallback to text output