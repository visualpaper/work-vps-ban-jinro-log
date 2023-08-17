from typing import Optional

from fastapi import Depends

from src.domain.user import User
from src.domain.user_repository import UserRepository
from src.infrastructure.repository.user_repository import UserRepositoryImpl


class UserFacade:
    def __init__(self, repository: UserRepository = Depends(UserRepositoryImpl)):
        self._repository = repository

    def get_user(self, sid: str) -> Optional[User]:
        return self._repository.find(sid)

    def create_user(self) -> User:
        sid: str = self._repository.create()

        return User(sid, [])
