from dataclasses import dataclass
from typing import List, Optional

from src.domain.village.village_cast import VillageCast
from src.domain.village.village_position import VillagePosition


@dataclass(frozen=True)
class VillageCondition:
    trip: Optional[str]
    people_min: Optional[int]
    people_max: Optional[int]
    casts: List[VillageCast]
    positions: List[VillagePosition]
    skip: int
    take: int
