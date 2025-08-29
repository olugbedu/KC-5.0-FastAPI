from starlette.middleware.base import BaseHTTPMiddleware
import logging

logger = logging.getLogger("notes_api")
logging.basicConfig(level=logging.INFO)


class RequestCounterMiddleware(BaseHTTPMiddleware):
    counter = 0

    async def dispatch(self, request, call_next):
        RequestCounterMiddleware.counter += 1
        logger.info(f"Total requests so far: {RequestCounterMiddleware.counter}")
        response = await call_next(request)
        return response
