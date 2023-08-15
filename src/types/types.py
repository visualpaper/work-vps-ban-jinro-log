from typing import List

import strawberry


@strawberry.type
class User:
    id: strawberry.ID
    villageNumbers: List[int]
