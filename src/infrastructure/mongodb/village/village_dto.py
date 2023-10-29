from typing import List, TypedDict

from bson import ObjectId


class VillageBansDto(TypedDict):
    position: str
    trip: str


class VillageDto(TypedDict):
    _id: ObjectId
    villageNumbers: List[int]
    endDate: int
    name: str
    people: int
    cast: str
    bans: List[VillageBansDto]
