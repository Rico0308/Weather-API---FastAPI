from api.v1.weather import router as weather_router
from fastapi import FastAPI

app = FastAPI(title="Weather API")

app.include_router(weather_router)
