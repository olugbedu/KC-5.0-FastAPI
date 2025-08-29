import time
from starlette.middleware.base import BaseHTTPMiddleware


class ResponseTimeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.time()
        response = await call_next(request)
        duration = time.time() - start
        response.headers["X-Response-Time"] = str(round(duration, 4)) + "s"
        return response
