from fastapi import APIRouter

from services.weather_service import weather_service

router = APIRouter(prefix="/weather", tags=["weather"])


@router.get("/{city}")
async def get_weather(city: str):
    return await weather_service.get_weather(city)
