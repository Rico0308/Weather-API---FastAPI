import httpx
from core.config import settings


class WeatherClient:
    def __init__(self) -> None:
        self._base_url = settings.weather_api_url
        self._api_key = settings.weather_api_key

    async def fetch(self, city: str) -> dict:
        url = f"{self._base_url}/{city}/today"
        params = {"key": self._api_key, "unitGroup": "metric", "include": "current"}

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params, timeout=10.0)
            response.raise_for_status()
            return response.json()


weather_client = WeatherClient()
