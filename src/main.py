import functools

import strawberry
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config.config import get_config
from .config.logger import get_logger
from .config.mongodb import close_mongo_connection, connect_to_mongo
from .exceptions.ban_jinro_log_exception_handler import MyGraphQLRouter
from .resolvers.context_getter import get_context
from .types.mutation import Mutation
from .types.query import Query

config = get_config()
logger = get_logger()


schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = MyGraphQLRouter(
    schema, graphiql=config.enable_graphiql, context_getter=get_context
)


# Application
app = FastAPI(title='ban jinro log API', version='1.0.0', docs_url=None, redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[config.cors_allow_origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB
app.add_event_handler("startup", functools.partial(connect_to_mongo, config=config))
app.add_event_handler("shutdown", close_mongo_connection)

# RateLimit とのインテグは strawberry 上特に見当たらなかったので一旦無しとしている。
app.include_router(graphql_app, prefix=config.graphql_endpoint)
logger.info("Ban Jinro Log Started")
