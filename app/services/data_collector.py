import httpx
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

async def fetch_market_data(sector: str) -> str:
    """
    Fetches real-time market-related news headlines for a given sector
    using DuckDuckGo HTML search and parses relevant results.
    """

    query = f"{sector} India market trends news"
    url = f"https://duckduckgo.com/html/?q={query}"

    async with httpx.AsyncClient(headers=HEADERS, timeout=10.0) as client:
        try:
            response = await client.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            results = []

            # Extract top search result titles
            for result in soup.select(".result__a")[:5]:
                title = result.get_text(strip=True)
                if title:
                    results.append(title)

            # Fallback if nothing found
            if not results:
                return f"No relevant market data found for {sector}"

            return "\n".join(results)

        except httpx.RequestError:
            return f"Error fetching data for {sector}"
        except Exception:
            return f"Unexpected error while fetching market data for {sector}"
