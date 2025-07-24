#!/usr/bin/env python3
"""
Virtual Assistant Main Application
Run this file to start the assistant
"""

import sys
import logging
from pathlib import Path

# Add src directory to path
sys.path.append(str(Path(__file__).parent))

from virtual_assistant import VirtualAssistant
from voice_interface import VoiceInterface, VOICE_AVAILABLE
from config.settings import Config

logger = logging.getLogger(__name__)

class AssistantApp:
    def __init__(self):
        self.assistant = VirtualAssistant()
        self.voice = VoiceInterface() if VOICE_AVAILABLE else None
        self.running = True
    
    def run_text_mode(self):
        """Run assistant in text-only mode"""
        print(f"\n🤖 {Config.ASSISTANT_NAME} Text Interface")
        print("Type 'quit', 'exit', or 'bye' to stop")
        print("Type 'voice' to switch to voice mode (if available)")
        print("-" * 50)
        
        while self.running:
            try:
                user_input = input("\nYou: ").strip()
                
                if not user_input:
                    continue
                
                # Check for exit commands
                if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                    print(f"\n{Config.ASSISTANT_NAME}: Goodbye! Have a great day!")
                    break
                
                # Check for voice mode switch
                if user_input.lower() == 'voice' and self.voice and hasattr(self.voice, 'available') and self.voice.available:
                    self.run_voice_mode()
                    continue
                elif user_input.lower() == 'voice':
                    print(f"{Config.ASSISTANT_NAME}: Voice mode is not available. The voice interface failed to initialize.")
                    continue
                
                # Process input
                response = self.assistant.process_text_input(user_input)
                print(f"{Config.ASSISTANT_NAME}: {response}")
                
            except KeyboardInterrupt:
                print(f"\n\n{Config.ASSISTANT_NAME}: Goodbye!")
                break
            except Exception as e:
                logger.error(f"Error in text mode: {e}")
                print(f"{Config.ASSISTANT_NAME}: Sorry, I encountered an error. Please try again.")
    
    def run_voice_mode(self):
        """Run assistant in voice mode"""
        if not self.voice or not hasattr(self.voice, 'available') or not self.voice.available:
            print("Voice mode is not available. The voice interface failed to initialize.")
            return
        
        print(f"\n🎤 {Config.ASSISTANT_NAME} Voice Interface")
        print("Say 'stop listening' or 'text mode' to switch back to text")
        print("Say 'goodbye' to quit")
        print("-" * 50)
        
        while self.running:
            try:
                # Listen for speech
                user_input = self.voice.listen_for_speech()
                
                if not user_input:
                    continue
                
                print(f"You said: {user_input}")
                
                # Check for mode switch or exit commands
                if any(phrase in user_input.lower() for phrase in ['stop listening', 'text mode']):
                    print("Switching to text mode...")
                    return
                
                if any(phrase in user_input.lower() for phrase in ['goodbye', 'quit', 'exit']):
                    response = "Goodbye! Have a great day!"
                    print(f"{Config.ASSISTANT_NAME}: {response}")
                    print("🔊 Speaking...")
                    self.voice.speak(response)
                    self.running = False
                    break
                
                # Process input
                response = self.assistant.process_text_input(user_input)
                print(f"{Config.ASSISTANT_NAME}: {response}")
                
                # Speak response and wait for completion
                print("🔊 Speaking...")
                self.voice.speak(response)
                print("🎤 Ready to listen again...")
                
            except KeyboardInterrupt:
                print(f"\n\n{Config.ASSISTANT_NAME}: Goodbye!")
                break
            except Exception as e:
                logger.error(f"Error in voice mode: {e}")
                print(f"{Config.ASSISTANT_NAME}: Sorry, I encountered an error.")

def main():
    """Main application entry point"""
    try:
        print("🚀 Starting Virtual Assistant...")
        
        # Initialize application
        app = AssistantApp()
        
        # Show available modes
        print("\nAvailable modes:")
        print("  • Text mode: Always available")
        voice_status = "Available" if (app.voice and app.voice.available) else "Not available (install speech libraries)"
        print(f"  • Voice mode: {voice_status}")
        
        # Start in text mode
        app.run_text_mode()
        
    except Exception as e:
        logger.error(f"Application startup error: {e}")
        print(f"Failed to start assistant: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()