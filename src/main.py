# src/main.py

from fastapi import FastAPI
from middlewares.ratelimiter import rate_limiter_middleware
from routes.api import router as api_router

app = FastAPI()

# Apply middleware
@app.middleware("http")
async def limit_middleware(request, call_next):
    ip = request.headers.get("X-Forwarded-For", request.client.host)
    print(f"[DEBUG] Request IP: {ip}")
    return await rate_limiter_middleware(request, call_next)

app.include_router(api_router, prefix="/api")