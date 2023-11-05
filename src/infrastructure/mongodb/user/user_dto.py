from datetime import date
from typing import List, TypedDict

from bson import ObjectId


class UserDto(TypedDict):
    _id: ObjectId
    villageNumbers: List[int]
    createDate: date  # mognodb ttl delete 都合 date 型にしている。
