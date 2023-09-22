import logging

from fastapi import FastAPI, Request
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app import limiter
from app.logs.logconfig import init_loggers

from .middleware import middlewareStack


# init our logger
init_loggers(logger_name="app-logs")
log = logging.getLogger("app-logs")

app = FastAPI(
    docs_url="/",
    middleware=middlewareStack,
)


app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.get('/health-check')
@limiter.limit("6/minute")
def health_check(request: Request) -> dict:
    return {'status': r'100% good'}
