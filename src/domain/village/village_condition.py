from dataclasses import dataclass
from typing import List, Optional

from src.domain.village.village_cast import VillageCast
from src.domain.village.village_position import VillagePosition


@dataclass(frozen=True)
class VillageCondition:
    # 制約として、
    # 以下条件が and で検索されるが、trip の人が cast/position で指定されたものとは限らない。
    # ※ Document が村別なので、本制約がある。ので村検索条件として利用すべき。
    trip: Optional[str]
    people_min: Optional[int]
    people_max: Optional[int]
    casts: List[VillageCast]
    positions: List[VillagePosition]
    skip: int
    take: int

    @classmethod
    def no_condition(cls, skip: int, take: int):
        return cls(
            trip=None,
            people_min=None,
            people_max=None,
            casts=[],
            positions=[],
            skip=skip,
            take=take,
        )
