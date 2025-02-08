from weather import WeatherForecast
from gpt_recommendation import GPTRecommendation
from email_handler import EmailNotifier
from email_template import format_forecast_email
from config import (
    OPENWEATHER_API_KEY, OPENAI_API_KEY, SENDER_EMAIL,
    RECEIVER_EMAIL, SMTP_USER, SMTP_PASS, SMTP_SERVER, SMTP_PORT
)

def main():
    weather_forecaster = WeatherForecast("Berlin", OPENWEATHER_API_KEY)
    gpt_recommender = GPTRecommendation(OPENAI_API_KEY)
    email_notifier = EmailNotifier(SENDER_EMAIL, RECEIVER_EMAIL, SMTP_USER, SMTP_PASS, SMTP_SERVER, SMTP_PORT)

    forecast = weather_forecaster.get_forecast()
    if forecast:
        email_content = format_forecast_email(forecast, gpt_recommender)
        email_notifier.send_email("🌍 3-Day Weather Forecast for Berlin", email_content)

if __name__ == "__main__":
    main()