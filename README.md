# weather--app# Weather Forecast Application

A fully functional Python weather application that fetches real-time weather data and forecasts using the OpenWeatherMap API...

## Features

✅ **Current Weather**: Get real-time weather information for any city
- Temperature (actual and "feels like")
- Weather conditions
- Humidity and pressure
- Wind speed
- Sunrise and sunset times

✅ **Weather Forecast**: Get 5-day weather forecasts
- Hourly breakdown for the first 24 hours
- Temperature trends
- Weather conditions
- Humidity tracking

✅ **User-Friendly Interface**: Interactive menu system

✅ **Error Handling**: Robust error handling for API requests

## Installation

### 1. Clone or navigate to the project directory
```bash
cd /workspaces/codespaces-blank/weather-app
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get an API Key

1. Go to [OpenWeatherMap API](https://openweathermap.org/api)
2. Sign up for a free account
3. Get your API key from the dashboard
4. Copy your API key

### 4. Configure the API Key

Edit `main.py` and replace the `API_KEY` value:
```python
API_KEY = "your_actual_api_key_here"
```

Or create a `.env` file:
```bash
cp .env.example .env
```

Then edit `.env` and add your actual API key.

## Usage

Run the application:
```bash
python main.py
```

The application will present a menu with options:
1. **Get current weather** - Enter a city name to see current conditions
2. **Get weather forecast** - Enter a city name to see the 5-day forecast
3. **Exit** - Close the application

### Examples

```
Enter city name: London
Enter city name: New York
Enter city name: Tokyo
```

## How It Works

### Architecture

The application uses an object-oriented approach with the `WeatherApp` class:

- **`__init__(api_key)`** - Initialize with your OpenWeatherMap API key
- **`get_current_weather(city)`** - Fetch current weather data
- **`get_forecast(city)`** - Fetch 5-day weather forecast
- **`display_current_weather()`** - Format and display current weather
- **`display_forecast()`** - Format and display forecast data

### API Integration

Uses the free OpenWeatherMap API:
- **Current Weather Endpoint**: `/weather`
- **Forecast Endpoint**: `/forecast`

### Data Processing

- Converts Unix timestamps to readable dates/times
- Formats temperatures in Celsius (configurable)
- Groups forecast data by day
- Displays data in an easy-to-read format

## Technical Details

- **Language**: Python 3.x
- **Key Libraries**: `requests` for HTTP calls
- **Type Hints**: Includes proper type annotations
- **Error Handling**: Try-except blocks for API failures

## Troubleshooting

### "Error fetching current weather"
- Verify your API key is correct
- Check your internet connection
- Ensure the city name is valid

### API Key Issues
- Sign up for a free account at openweathermap.org
- Wait a few minutes after registration for the key to activate
- Check that you copied the entire key correctly

### Network Issues
- Check your internet connection
- Verify the OpenWeatherMap API is not down
- Try a different city

## Future Enhancements

- Add caching to reduce API calls
- Store favorite cities
- Add weather alerts
- Support for coordinates (latitude/longitude)
- Export data to CSV/JSON
- Add weather icons/emojis for conditions
- Background tasks for periodic updates
- Web UI using Flask/Django

## License

This project is open source and available for educational purposes.

---
.
**Enjoy using the Weather Forecast Application!** 🌤️
