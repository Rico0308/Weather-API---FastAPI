from clients.weather_client import weather_client
from services.cache_service import cache_service


class WeatherService:
    async def get_weather(self, city: str) -> dict:
        cache_key = f"weather:{city.lower()}"

        cached = await cache_service.get(cache_key)
        if cached is not None:
            return cached

        data = await weather_client.fetch(city)
        await cache_service.set(cache_key, data)
        return data


weather_service = WeatherService()
