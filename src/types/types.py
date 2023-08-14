import strawberry

from typing import List


@strawberry.type
class User:
    id: strawberry.ID
    villageNumbers: List[int]
