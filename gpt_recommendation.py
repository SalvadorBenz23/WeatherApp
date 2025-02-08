import openai

class GPTRecommendation:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_recommendation(self, weather_condition, date):
        """Fetch a GPT-based recommendation for after-work activities."""
        prompt = f"""
        The weather in Berlin on {date} is expected to be {weather_condition}. Suggest a fun afterwork activity for colleagues,
        prioritizing outdoor options if possible, and make the recommendation concise and friendly.
        """
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert on Berlin activity recommendations."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100,
            )
            return response.choices[0].message.content.strip()
        except openai.OpenAIError as e:
            print(f"❌ Error with OpenAI request: {e}")
            return "Couldn't fetch recommendations due to an API issue."