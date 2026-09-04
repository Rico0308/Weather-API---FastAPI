from core.config import settings
from core.limiter import limiter
from fastapi import APIRouter, Request
from services.weather_service import weather_service

router = APIRouter(prefix="/weather", tags=["weather"])


@router.get("/{city}")
@limiter.limit(settings.rate_limit)
async def get_weather(request: Request, city: str):
    return await weather_service.get_weather(city)
