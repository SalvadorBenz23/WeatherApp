from utils import get_weather_icon

def format_forecast_email(forecast, gpt_recommender):
    """Format the forecast and recommendations into an HTML email."""
    email_content = f"""
    <html>
        <head>
            <style>
                table {{
                    width: 100%;
                    border-collapse: collapse;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
            </style>
        </head>
        <body>
            <h1>🌤️ 3-Day Weather Forecast for Berlin 🌤️</h1>
            <p><b>Hi Lisa,</b></p>
            <p>Here’s your personalized weather update for the next three days in Berlin! 🌤️ Use this to plan your day and after-work activities.</p>
    """
    for date, entries in forecast.items():
        email_content += f"""
            <h2>📅 {date}</h2>
            <table>
                <thead>
                    <tr>
                        <th>Time</th>
                        <th>Temperature (°C)</th>
                        <th>Conditions</th>
                        <th>Humidity (%)</th>
                        <th>Wind Speed (m/s)</th>
                    </tr>
                </thead>
                <tbody>
        """
        for entry in entries:
            icon = get_weather_icon(entry["description"])
            email_content += f"""
                <tr>
                    <td>{entry['time']}</td>
                    <td>{entry['temperature']}°C</td>
                    <td>{icon} {entry['description']}</td>
                    <td>{entry['humidity']}</td>
                    <td>{entry['wind_speed']}</td>
                </tr>
            """
        weather_condition = entries[-1]["description"] if entries else "clear sky"
        gpt_recommendation = gpt_recommender.get_recommendation(weather_condition, date)
        email_content += f"""
                </tbody>
            </table>
            <p><b>✨ GPT Recommendation:</b> {gpt_recommendation}</p>
        """

    email_content += "<p><b>Stay safe and enjoy your day! Don’t hesitate to reach out if you have any questions. 🌍</b></p></body></html>"
    return email_content