from typing import Optional

from src.domain.user import User
from src.domain.user_repository import UserRepository


class UserRepositoryImpl(UserRepository):
    def find(self, sid: str) -> Optional[User]:
        # db = get_database()
        # print(db["tm_user"].count_documents({}))
        pass

    def insert(self) -> str:
        pass
