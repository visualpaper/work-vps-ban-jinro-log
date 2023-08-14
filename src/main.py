import strawberry

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from .types.query import Query
from .types.mutation import Mutation

from .config.config import get_config
from .config.logger import get_logger
from .config.rate_limiter import get_limiter

config = get_config()
limiter = get_limiter()
logger = get_logger()

schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema, graphiql=config.enable_graphiql)


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
app.include_router(graphql_app, prefix=config.graphql_endpoint)

logger.info("Ban Jinro Log Started")
