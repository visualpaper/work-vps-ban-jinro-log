from datetime import datetime
from typing import Optional

from bson import ObjectId
from fastapi import Depends

from src.domain.user.user import User
from src.domain.user.user_repository import UserRepository
from src.infrastructure.mongodb.user.user_dao import UserDao
from src.infrastructure.mongodb.user.user_dto import UserDto


class UserRepositoryImpl(UserRepository):
    def __init__(self, dao: UserDao = Depends(UserDao)):
        self._dao = dao

    def find(self, sid: str) -> Optional[User]:
        dto: Optional[UserDto] = self._dao.find_one(sid)
        if dto is not None:
            return User(_id=str(dto["_id"]), _village_numbers=dto["villageNumbers"])

    def create(self) -> str:
        dto: UserDto = UserDto(
            _id=ObjectId(), villageNumbers=[], createData=datetime.now()
        )

        self._dao.insert_one(dto)
        return str(dto["_id"])
