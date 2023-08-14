import strawberry

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .types.query import Query
from .types.mutation import Mutation

from .exceptions.ban_jinro_log_exception_handler import MyGraphQLRouter

from .config.config import get_config
from .config.logger import get_logger

config = get_config()
logger = get_logger()

schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = MyGraphQLRouter(schema, graphiql=config.enable_graphiql)


# Application
app = FastAPI(title='ban jinro log API', version='1.0.0', docs_url=None, redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[config.cors_allow_origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# RateLimit とのインテグは strawberry 上特に見当たらなかったので一旦無しとしている。
app.include_router(graphql_app, prefix=config.graphql_endpoint)
logger.info("Ban Jinro Log Started")
