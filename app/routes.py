from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import PlainTextResponse

from app.utils.validators import validate_sector
from app.auth import verify_token
from app.rate_limiter import check_rate_limit
from app.services.data_collector import fetch_market_data
from app.services.ai_analyzer import analyze_data
from app.services.report_generator import generate_markdown

router = APIRouter()

@router.get("/analyze/{sector}", response_class=PlainTextResponse)
async def analyze_sector(sector: str, user=Depends(verify_token)):

    # ✅ Input validation
    if not validate_sector(sector):
        raise HTTPException(status_code=400, detail="Invalid sector name")

    user_id = user.get("user")

    # ✅ Rate limiting
    if not check_rate_limit(user_id):
        raise HTTPException(status_code=429, detail="Too many requests. Try again later.")

    try:
        # 🌐 Fetch market data
        data = await fetch_market_data(sector)

        # 🤖 AI analysis
        analysis = await analyze_data(sector, data)

        # 📝 Generate markdown report
        report = generate_markdown(sector, analysis)

        return report

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")