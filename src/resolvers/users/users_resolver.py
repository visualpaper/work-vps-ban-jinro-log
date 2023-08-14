import strawberry

from src.types.types import User


def initialize() -> User:
    return User(id=strawberry.ID("aaa"), villageNumbers=[])
