from datetime import date
from typing import List, TypedDict

from bson import ObjectId


class UserDto(TypedDict):
    _id: ObjectId
    villageNumbers: List[int]
    createData: date
