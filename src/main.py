from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config.config import get_config
from .config.logger import get_logger
from .config.rate_limiter import get_limiter

config = get_config()
limiter = get_limiter()
logger = get_logger()


# Application
app = FastAPI(
    title='image-converter API', version='1.0.0', docs_url=None, redoc_url=None
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[config.cors_allow_origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add RateLimit
app.state.limiter = limiter

logger.info("Image Converter Started")
