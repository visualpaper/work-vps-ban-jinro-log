from typing import List

from strawberry.types import Info

from src.types.types import Village


def list_villages(info: Info, skip: int = 0, take: int = 5) -> List[Village]:
    print(skip)
    print(take)
    return []
