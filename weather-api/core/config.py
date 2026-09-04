from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0

    weather_api_key: str
    weather_api_url: str = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"

    cache_ttl_seconds: int = 300

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
