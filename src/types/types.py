from typing import List

import strawberry


@strawberry.type(name="User")
class UserSchema:
    id: strawberry.ID
    villageNumbers: List[int]
