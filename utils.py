def get_weather_icon(description):
    """Return an emoji icon based on weather conditions."""
    if "rain" in description.lower():
        return "☔"
    elif "clear" in description.lower():
        return "☀️"
    elif "cloud" in description.lower():
        return "☁️"
    elif "snow" in description.lower():
        return "❄️"
    elif "storm" in description.lower():
        return "🌩️"
    else:
        return "🌍"