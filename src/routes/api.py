from fastapi import APIRouter, Request
from models.users import get_user

router = APIRouter()

@router.get("/public")
async def public():
    return "Public API response"

@router.get("/user-info")
async def user_info(request: Request):
    user = get_user(request.client.host)
    return {
        "ip": request.client.host,
        "group": user["group"],
        "rate_limit": {
            "gold": 10,
            "silver": 2,
            "bronze": 5,
            "default": 2
        }.get(user["group"], 2)
    }