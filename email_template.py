from utils import get_weather_icon

def format_forecast_email(forecast, gpt_recommender):
    """Format the forecast email with improved reliability and simplicity."""
    email_content = f"""
    <html>
        <body>
            <table style="width: 100%; border: none; margin-bottom: 20px;">
                <tr>
                    <td align="center">
                        <h1 style="margin: 0;">🌤️ 3-Day Weather Forecast for Berlin 🌤️</h1>
                    </td>
                </tr>
                <tr>
                    <td>
                        <p style="margin: 10px 0; font-family: Arial, sans-serif; font-size: 14px;">
                            <b>Hello Lisa,</b><br>
                            Here’s your daily weather update for the next three days in Berlin! Plan your day with the forecast and check out our GPT-powered recommendations below.
                        </p>
                    </td>
                </tr>
            </table>
    """

    for date, entries in forecast.items():
        email_content += f"""
            <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px; font-family: Arial, sans-serif; font-size: 14px;">
                <thead>
                    <tr>
                        <th colspan="5" style="background-color: #f4f4f4; padding: 10px; text-align: center;">
                            📅 Weather Forecast for {date}
                        </th>
                    </tr>
                    <tr style="background-color: #e0e0e0;">
                        <th style="padding: 8px; border: 1px solid #ddd;">Time</th>
                        <th style="padding: 8px; border: 1px solid #ddd;">Temp (°C)</th>
                        <th style="padding: 8px; border: 1px solid #ddd;">Conditions</th>
                        <th style="padding: 8px; border: 1px solid #ddd;">Humidity (%)</th>
                        <th style="padding: 8px; border: 1px solid #ddd;">Wind Speed (m/s)</th>
                    </tr>
                </thead>
                <tbody>
        """
        evening_icon = "🌍"
        for entry in entries:
            icon = get_weather_icon(entry["description"])
            if entry["time"] == "18:00":
                evening_icon = icon
            email_content += f"""
                    <tr>
                        <td style="padding: 8px; border: 1px solid #ddd;">{entry['time']}</td>
                        <td style="padding: 8px; border: 1px solid #ddd;">{entry['temperature']}°C</td>
                        <td style="padding: 8px; border: 1px solid #ddd;">{icon} {entry['description']}</td>
                        <td style="padding: 8px; border: 1px solid #ddd;">{entry['humidity']}</td>
                        <td style="padding: 8px; border: 1px solid #ddd;">{entry['wind_speed']}</td>
                    </tr>
            """
        weather_condition = entries[-1]["description"] if entries else "clear sky"
        gpt_recommendation = gpt_recommender.get_recommendation(weather_condition, date)
        email_content += f"""
                </tbody>
            </table>
            <p style="font-family: Arial, sans-serif; font-size: 14px;">
                <b>✨ GPT Recommendation ({evening_icon} on {date}):</b> {gpt_recommendation}
            </p>
        """

    email_content += """
            <p style="font-family: Arial, sans-serif; font-size: 14px; margin-top: 20px;">
                <b>Stay safe and have a great day! 🌍</b>
            </p>
        </body>
    </html>
    """
    return email_content