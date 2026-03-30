import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def analyze_data(sector, data):
    try:
        prompt = f"""
        Analyze the Indian {sector} sector.

        Provide:
        - Market Trends
        - Key Opportunities
        - Risks
        - Trade Ideas

        Data:
        {data}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ AI Error: {str(e)}"