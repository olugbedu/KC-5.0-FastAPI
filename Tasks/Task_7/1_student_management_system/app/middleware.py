from starlette.middleware.base import BaseHTTPMiddleware
import logging

logging.basicConfig(filename="requests.log", level=logging.INFO)


class RequestLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        logging.info(f"{request.method} {request.url}")
        response = await call_next(request)
        return response
