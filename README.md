# Weather API

FastAPI service that fetches weather data from Visual Crossing (3rd party API) and caches responses in Redis.
- Project URL: https://roadmap.sh/projects/weather-api-wrapper-service

## Requirements

- [Python 3.13+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) — Python package manager
- [Docker](https://docs.docker.com/get-docker/) — to run Redis
- A [Visual Crossing](https://www.visualcrossing.com/weather-api) API key (free tier available)

## Setup

1. Clone the repo and enter the project folder:

   ```bash
   cd weather-api
   ```

2. Install dependencies:

   ```bash
   uv sync
   ```

3. Copy the env template and fill in your API key:

   ```bash
   cp .env.example .env
   ```

   Edit `.env` and set `WEATHER_API_KEY` with your Visual Crossing key.

4. Start Redis with Docker:

   ```bash
   docker run -d --name weather-redis -p 6379:6379 redis:alpine
   ```

   To stop/start it later:

   ```bash
   docker stop weather-redis
   docker start weather-redis
   ```

5. Run the API:

   ```bash
   uv run fastapi dev main.py
   ```

6. Test it:

   ```bash
   curl http://localhost:8000/weather/Bogota
   ```

   Or open [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive Swagger UI.

## Environment variables

| Variable             | Required | Default                                                                  | Description                             |
| --------------------- | -------- | ------------------------------------------------------------------------- | ---------------------------------------- |
| `WEATHER_API_KEY`    | yes      | —                                                                         | Visual Crossing API key                  |
| `WEATHER_API_URL`    | no       | `https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline` | Visual Crossing base URL                 |
| `REDIS_HOST`         | no       | `localhost`                                                              | Redis host                               |
| `REDIS_PORT`         | no       | `6379`                                                                   | Redis port                               |
| `REDIS_DB`           | no       | `0`                                                                      | Redis DB index                           |
| `CACHE_TTL_SECONDS`  | no       | `300`                                                                    | How long a cached weather response lives |

See `.env.example` for a ready-to-copy template.

## Project structure

```
weather-api/
├── main.py                 # creates the app, mounts routers
├── core/
│   └── config.py           # Settings (env vars via pydantic-settings)
├── clients/
│   └── weather_client.py   # HTTP calls to Visual Crossing
├── services/
│   ├── cache_service.py    # Redis get/set wrapper
│   └── weather_service.py  # orchestrates cache -> 3rd party -> cache
└── api/v1/
    └── weather.py          # GET /weather/{city}
```
