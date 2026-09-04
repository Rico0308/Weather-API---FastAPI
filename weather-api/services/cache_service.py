import json

import redis.asyncio as redis
from core.config import settings


class CacheService:
    def __init__(self) -> None:
        self._client = redis.Redis(
            host=settings.redis_host,
            port=settings.redis_port,
            db=settings.redis_db,
            decode_responses=True,
        )

    async def get(self, key: str) -> dict | None:
        raw = await self._client.get(key)
        return json.loads(raw) if raw else None

    async def set(self, key: str, value: dict) -> None:
        await self._client.set(key, json.dumps(value), ex=settings.cache_ttl_seconds)


cache_service = CacheService()
