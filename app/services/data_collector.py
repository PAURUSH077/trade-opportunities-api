import httpx

async def fetch_market_data(sector: str):
    query = f"{sector} India market trends news"

    url = f"https://duckduckgo.com/?q={query}"

    async with httpx.AsyncClient() as client:
        try:
            res = await client.get(url)
            return res.text[:2000]   # limit data
        except:
            return "No market data found"