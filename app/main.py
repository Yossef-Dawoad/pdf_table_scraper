import logging
from contextlib import asynccontextmanager

import spacy
from fastapi import FastAPI, Request
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.limit_config import limiter
from app.logs.logconfig import init_loggers
from app.scraper.routes import router as scraper_router

from .middleware import middlewareStack

# api rate limiting
# limiter = Limiter(
#     key_func=get_remote_address,
#     default_limits=["60/minute"],
#     strategy='fixed-window-elastic-expiry',
# )

# init our logger
init_loggers(logger_name="app-logs")
log = logging.getLogger("app-logs")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    nlp_model = spacy.load('en_core_web_sm')

    yield {'ner_model': nlp_model}


app = FastAPI(
    docs_url="/",
    middleware=middlewareStack,
    lifespan=lifespan,
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# nlp = spacy.load('en_core_web_sm')
app.include_router(scraper_router)


@app.get('/health-check')
@limiter.limit("6/minute")
def health_check(request: Request) -> dict:
    return {'status': r'100% good'}
