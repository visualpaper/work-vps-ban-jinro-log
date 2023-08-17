from typing import Optional

from bson import ObjectId
from fastapi import Depends
from pymongo.collection import Collection
from pymongo.database import Database

from src.config.mongodb import get_database
from src.infrastructure.mongodb.user_dto import UserDto


class UserDao:
    def __init__(self, db: Database = Depends(get_database)):
        self._collection: Collection = db["tm_user"]

    def find_one(self, sid: str) -> Optional[UserDto]:
        return self._collection.find_one(ObjectId(sid))

    def insert_one(self, dto: UserDto):
        self._collection.insert_one(dto)
