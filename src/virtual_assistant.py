import logging
from datetime import datetime
from typing import Optional
import sys
import os

import openai
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.settings import Config

# Configure logging
logging.basicConfig(level=getattr(logging, Config.LOG_LEVEL))
logger = logging.getLogger(__name__)

class VirtualAssistant:
    def __init__(self):
        """Initialize the virtual assistant with configuration"""
        Config.validate()
        
        # Initialize OpenAI client
        self.client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
        
        # Assistant settings
        self.name = Config.ASSISTANT_NAME
        self.conversation_history = []
        
        # Initialize capabilities
        self.capabilities = {
            'weather': self._get_weather,
            'time': self._get_current_time,
            'calculation': self._calculate,
            'reminder': self._set_reminder,
            'joke': self._tell_joke
        }
        
        logger.info(f"Virtual Assistant '{self.name}' initialized successfully")
    
    def process_text_input(self, user_input: str) -> str:
        """Process text input and return response"""
        logger.info(f"Processing input: {user_input}")
        
        # Add to conversation history
        self.conversation_history.append({"role": "user", "content": user_input})
        
        # Check for specific capabilities first
        response = self._check_capabilities(user_input)
        
        if not response:
            # Use OpenAI for general conversation
            response = self._generate_ai_response(user_input)
        
        # Add response to history
        self.conversation_history.append({"role": "assistant", "content": response})
        
        # Keep history manageable (last 10 exchanges)
        if len(self.conversation_history) > 20:
            self.conversation_history = self.conversation_history[-20:]
        
        logger.info(f"Generated response: {response}")
        return response
    
    def _check_capabilities(self, user_input: str) -> Optional[str]:
        """Check if input matches specific capabilities"""
        user_input_lower = user_input.lower()
        
        if any(word in user_input_lower for word in ['weather', 'temperature', 'forecast']):
            return self.capabilities['weather'](user_input)
        elif any(word in user_input_lower for word in ['time', 'clock', 'hour']):
            return self.capabilities['time']()
        elif any(word in user_input_lower for word in ['calculate', 'math', '+', '-', '*', '/']):
            return self.capabilities['calculation'](user_input)
        elif any(word in user_input_lower for word in ['remind', 'reminder', 'schedule']):
            return self.capabilities['reminder'](user_input)
        elif any(word in user_input_lower for word in ['joke', 'funny', 'laugh']):
            return self.capabilities['joke']()
        
        return None
    
    def _generate_ai_response(self, user_input: str) -> str:
        """Generate AI response using OpenAI"""
        try:
            # Create system message for context
            system_message = {
                "role": "system",
                "content": f"You are {self.name}, a helpful virtual assistant. "
                          "Keep responses concise but friendly. "
                          "If asked about capabilities, mention weather, time, calculations, reminders, and jokes."
            }
            
            # Prepare messages for API call
            messages = [system_message] + self.conversation_history[-10:]  # Last 5 exchanges
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=150,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            logger.error(f"Error generating AI response: {e}")
            return "I'm sorry, I'm having trouble processing that right now. Please try again."
    
    def _get_weather(self, query: str) -> str:
        """Get weather information"""
        if not Config.WEATHER_API_KEY:
            return "Weather service is not configured. Please add WEATHER_API_KEY to .env file."
        
        # Extract city from query
        city = self._extract_city_from_query(query)
        if not city:
            return "Please specify a city for weather information. For example: 'weather in Paris' or 'London weather'"
        
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={Config.WEATHER_API_KEY}&units=metric"
            response = requests.get(url, timeout=5)
            data = response.json()
            
            if response.status_code == 200:
                temp = data['main']['temp']
                description = data['weather'][0]['description']
                city_name = data['name']
                country = data['sys']['country']
                return f"The weather in {city_name}, {country} is {temp}°C with {description}."
            else:
                return f"Sorry, I couldn't find weather information for '{city}'. Please check the city name and try again."
                
        except Exception as e:
            logger.error(f"Weather API error: {e}")
            return "Sorry, I'm having trouble accessing weather information right now."
    
    def _extract_city_from_query(self, query: str) -> str:
        """Extract city name from weather query"""
        query_lower = query.lower()
        words = query_lower.split()
        
        # Remove common weather-related words
        weather_words = {'weather', 'forecast', 'temperature', 'temp', 'in', 'for', 'at', 'the', 'what', 'is', 'how', 'tell', 'me', 'about'}
        
        # Filter out weather words to find potential city names
        potential_cities = [word for word in words if word not in weather_words]
        
        # Join remaining words as they might be a multi-word city name
        if potential_cities:
            return ' '.join(potential_cities)
        
        return None
    
    def _get_current_time(self) -> str:
        """Get current time"""
        now = datetime.now()
        return f"The current time is {now.strftime('%H:%M:%S')} on {now.strftime('%Y-%m-%d')}."
    
    def _calculate(self, query: str) -> str:
        """Perform basic calculations"""
        try:
            # Extract mathematical expression (basic implementation)
            # This is a simplified version - in production, use a proper math parser
            import re
            
            # Find numbers and operators
            expression = re.sub(r'[^\d+\-*/().\s]', '', query)
            expression = expression.strip()
            
            if expression:
                # Safe evaluation (limited scope)
                allowed_chars = set('0123456789+-*/(). ')
                if all(c in allowed_chars for c in expression):
                    result = eval(expression)
                    return f"The result is: {result}"
            
            return "I couldn't find a valid mathematical expression in your request."
            
        except Exception as e:
            logger.error(f"Calculation error: {e}")
            return "Sorry, I couldn't perform that calculation."
    
    def _set_reminder(self, query: str) -> str:
        """Set a simple reminder (basic implementation)"""
        # This is a simplified version - in production, integrate with calendar APIs
        logger.info(f"Reminder requested: {query}")
        return "I've noted your reminder request. In a full implementation, this would integrate with your calendar system."
    
    def _tell_joke(self) -> str:
        """Tell a random joke"""
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the computer go to the doctor? Because it had a virus!",
            "Why don't programmers like nature? It has too many bugs!",
            "What do you call a computer that sings? A-Dell!",
            "Why do robots never panic? They have nerves of steel!"
        ]
        import random
        return random.choice(jokes)