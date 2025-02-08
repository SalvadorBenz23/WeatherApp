import requests
from datetime import datetime, timedelta, timezone

class WeatherForecast:
    def __init__(self, city, api_key):
        self.city = city
        self.api_key = api_key
        self.endpoint = "https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}&units=metric"

    def get_forecast(self):
        """Fetch the 3-day weather forecast."""
        url = self.endpoint.format(self.city, self.api_key)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return self._process_forecast(data)
        else:
            print(f"❌ Error fetching weather data: {response.status_code}")
            return None

    def _process_forecast(self, data):
        """Process raw forecast data into a structured format."""
        forecast = {}
        today = datetime.now(timezone.utc).date()
        for day_offset in range(1, 4):  # Generate dates for the next 3 days
            date = today + timedelta(days=day_offset)
            forecast[str(date)] = []

        for entry in data["list"]:
            timestamp = datetime.strptime(entry["dt_txt"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
            if str(timestamp.date()) in forecast and 9 <= timestamp.hour <= 21:
                forecast[str(timestamp.date())].append({
                    "time": timestamp.strftime("%H:%M"),
                    "temperature": entry["main"]["temp"],
                    "description": entry["weather"][0]["description"],
                    "humidity": entry["main"]["humidity"],
                    "wind_speed": entry["wind"]["speed"]
                })
        return forecast