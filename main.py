#!/usr/bin/env python3
"""
Weather Forecast Application
A functional weather app that fetches current weather and forecasts using OpenWeatherMap API
"""
import os
import requests
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional


class WeatherApp:
    """Main weather application class"""
    
    BASE_URL = "https://api.openweathermap.org/data/2.5"
    
    def __init__(self, api_key: str):
        """Initialize the weather app with an API key"""
        self.api_key = api_key
        self.current_weather = None
        self.forecast = None
        
    def get_current_weather(self, city: str) -> Optional[Dict]:
        """
        Fetch current weather for a given city
        
        Args:
            city: City name
            
        Returns:
            Dictionary with weather data or None if request fails
        """
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'
            }
            response = requests.get(f"{self.BASE_URL}/weather", params=params, timeout=5)
            response.raise_for_status()
            self.current_weather = response.json()
            return self.current_weather
        except requests.exceptions.RequestException as e:
            print(f"⚠️  API Error: {e}")
            print(f"📌 Using demo data (get API key from openweathermap.org)")
            # Return mock data for demo purposes
            self.current_weather = self.get_mock_current_weather(city)
            return self.current_weather
    
    def get_forecast(self, city: str, days: int = 5) -> Optional[Dict]:
        """
        Fetch weather forecast for a given city
        
        Args:
            city: City name
            days: Number of days to forecast (default 5)
            
        Returns:
            Dictionary with forecast data or None if request fails
        """
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric',
                'cnt': days * 8  # API returns data in 3-hour intervals
            }
            response = requests.get(f"{self.BASE_URL}/forecast", params=params, timeout=5)
            response.raise_for_status()
            self.forecast = response.json()
            return self.forecast
        except requests.exceptions.RequestException as e:
            print(f"⚠️  API Error: {e}")
            print(f"📌 Using demo data (get API key from openweathermap.org)")
            # Return mock data for demo purposes
            self.forecast = self.get_mock_forecast(city)
            return self.forecast
    
    def display_current_weather(self) -> None:
        """Display current weather in a formatted way"""
        if not self.current_weather:
            print("No current weather data. Please fetch it first.")
            return
        
        data = self.current_weather
        print("\n" + "="*50)
        print(f"🌍 CURRENT WEATHER - {data['name']}, {data['sys']['country']}")
        print("="*50)
        
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']
        
        print(f"Temperature:     {main['temp']}°C (feels like {main['feels_like']}°C)")
        print(f"Condition:       {weather['main']} - {weather['description']}")
        print(f"Humidity:        {main['humidity']}%")
        print(f"Pressure:        {main['pressure']} hPa")
        print(f"Wind Speed:      {wind['speed']} m/s")
        print(f"Cloudiness:      {data['clouds']['all']}%")
        print(f"Sunrise:         {datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')}")
        print(f"Sunset:          {datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')}")
        print("="*50 + "\n")
    
    def display_forecast(self) -> None:
        """Display weather forecast in a formatted way"""
        if not self.forecast:
            print("No forecast data. Please fetch it first.")
            return
        
        data = self.forecast
        print("\n" + "="*50)
        print(f"📅 WEATHER FORECAST - {data['city']['name']}")
        print("="*50)
        
        current_date = None
        for item in data['list'][:24]:  # Show first 24 hours
            dt = datetime.fromtimestamp(item['dt'])
            date = dt.strftime('%Y-%m-%d')
            time = dt.strftime('%H:%M')
            
            if current_date != date:
                current_date = date
                print(f"\n📅 {date}")
                print("-" * 50)
            
            temp = item['main']['temp']
            feels = item['main']['feels_like']
            weather = item['weather'][0]['main']
            humidity = item['main']['humidity']
            
            print(f"  {time} - {temp}°C (feels {feels}°C) | {weather} | 💧 {humidity}%")
        
        print("="*50 + "\n")


    def get_mock_current_weather(self, city: str) -> Optional[Dict]:
        """Generate mock current weather data for demo"""
        now = datetime.now()
        return {
            "name": city,
            "sys": {
                "country": "GB",
                "sunrise": int((now - timedelta(hours=6)).timestamp()),
                "sunset": int((now + timedelta(hours=6)).timestamp())
            },
            "main": {
                "temp": 12.5,
                "feels_like": 10.2,
                "humidity": 75,
                "pressure": 1013
            },
            "weather": [{
                "main": "Cloudy",
                "description": "overcast clouds"
            }],
            "wind": {"speed": 5.2},
            "clouds": {"all": 85}
        }
    
    def get_mock_forecast(self, city: str) -> Optional[Dict]:
        """Generate mock forecast data for demo"""
        now = datetime.now()
        forecast_list = []
        
        for i in range(8):
            dt = now + timedelta(hours=i*3)
            forecast_list.append({
                "dt": int(dt.timestamp()),
                "main": {
                    "temp": 12 + i - 2,
                    "feels_like": 10 + i - 2,
                    "humidity": 70 + (i % 3) * 5
                },
                "weather": [{
                    "main": ["Sunny", "Cloudy", "Rainy"][i % 3]
                }]
            })
        
        return {
            "city": {"name": city},
            "list": forecast_list
        }


def main():
    """Main function to run the weather app"""
    
    # Get your free API key from: https://openweathermap.org/api
    # Sign up at: https://openweathermap.org/api
API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    print("❌ API key not found.")
    print("Set OPENWEATHER_API_KEY as an environment variable.")
    # Replace with your actual API key
    
    app = WeatherApp(API_KEY)
    
    print("\n🌤️  WEATHER FORECAST APPLICATION 🌤️")
    print("=" * 50)
    print("Note: Using demo data (get' real API key from openweathermap.org)")
    
    while True:
        print("\nOptions:")
        print("1. Get current weather")
        print("2. Get weather forecast")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            city = input("Enter city name: ").strip()
            if city:
                print(f"\n⏳ Fetching current weather for {city}...")
                if app.get_current_weather(city):
                    app.display_current_weather()
                else:
                    print(f"❌ Could not fetch weather for {city}")
        
        elif choice == '2':
            city = input("Enter city name: ").strip()
            if city:
                print(f"\n⏳ Fetching forecast for {city}...")
                if app.get_forecast(city):
                    app.display_forecast()
                else:
                    print(f"❌ Could not fetch forecast for {city}")
        
        elif choice == '3':
            print("\n👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
