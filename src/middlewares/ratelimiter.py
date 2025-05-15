from fastapi import Request, Response, HTTPException
import asyncio
from config.redis import redis_client
from models.users import get_user

GROUP_LIMITS = {
    "gold": 10,
    "silver": 2,
    "bronze": 5,
    "default": 2
}

async def rate_limiter_middleware(request, call_next):
  

    ip = request.client.host
    user = get_user(ip)
    group = user.get("group", "default")
    limit = GROUP_LIMITS.get(group, GROUP_LIMITS["default"])

    key = f"rate_limit:{group}:{ip}"

    current = await redis_client.get(key)

    if current and int(current) >= limit:
        print(f"[RATELIMIT] IP={ip}, Group={group} exceeded limit")
        return Response("Too Many Requests", status_code=429)

    if not current:
        await redis_client.setex(key, 60, 1)
    else:
        await redis_client.incr(key)

    return await call_next(request)