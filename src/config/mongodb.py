from motor import motor_asyncio

from src.config.config import Settings


class DataBase:
    client: motor_asyncio.AsyncIOMotorClient = None
    database: motor_asyncio.AsyncIOMotorDatabase


db = DataBase()


async def connect_to_mongo(config: Settings):
    db.client = motor_asyncio.AsyncIOMotorClient(
        str(config.mongodb_url),
        maxPoolSize=config.mongodb_max_connection_pool,
        minPoolSize=config.mongodb_min_connection_pool,
    )
    db.database = motor_asyncio.AsyncIOMotorDatabase = db.client[config.mongodb_dbname]


async def close_mongo_connection():
    db.client.close()


async def get_database() -> motor_asyncio.AsyncIOMotorDatabase:
    return db.database
