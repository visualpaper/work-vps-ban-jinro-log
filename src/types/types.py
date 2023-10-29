from enum import Enum
from typing import List, Optional

import strawberry


@strawberry.type(name="User")
class UserSchema:
    id: strawberry.ID
    villageNumbers: List[int]


@strawberry.enum
class VillagePosition(Enum):
    WOLF = "人狼"
    FANATIC = "狂信者"
    MADMAN = "狂人"
    FOX = "妖狐"
    APOSTATE = "背徳者"
    SEER = "占い師"
    MEDIUM = "霊能"
    HUNTER = "狩人"
    CAT = "猫又"
    MASON = "共有"
    VILLAGER = "村人"


@strawberry.enum
class VillageCast(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    Z = "Z"


@strawberry.type(name="VillageBans")
class VillageBans:
    position: VillagePosition
    trip: str


@strawberry.type(name="Village")
class Village:
    id: strawberry.ID
    number: str
    endDate: str
    url: str
    name: str
    people: int
    cast: VillageCast
    bans: List[VillageBans]


@strawberry.input
class VillagesInput:
    trip: Optional[str] = None
    people_min: Optional[int] = None
    people_max: Optional[int] = None
    cast: List[VillageCast]
    position: List[VillagePosition]
    skip: int = 0
    take: int = 5
