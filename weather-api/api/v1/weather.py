from clients.weather_client import weather_client
from fastapi import APIRouter

router = APIRouter(prefix="/weather", tags=["weather"])


@router.get("/{city}")
async def get_weather(city: str):
    return await weather_client.fetch(city)
