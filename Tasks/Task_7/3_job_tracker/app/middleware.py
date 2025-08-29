from fastapi import Request, HTTPException


async def check_user_agent(request: Request, call_next):
    if "user-agent" not in request.headers:
        raise HTTPException(status_code=400, detail="User-Agent header required")
    response = await call_next(request)
    return response
