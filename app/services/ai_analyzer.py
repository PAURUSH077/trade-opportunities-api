import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Initialize Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

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

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error analyzing data: {str(e)}"