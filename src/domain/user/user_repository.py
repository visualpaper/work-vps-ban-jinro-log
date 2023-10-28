from abc import ABC, abstractmethod
from typing import Optional

from src.domain.user.user import User


class UserRepository(ABC):
    @abstractmethod
    def create(self) -> str:
        pass

    @abstractmethod
    def find(self, sid: str) -> Optional[User]:
        pass
