from dataclasses import dataclass
from typing import List

from src.domain.utc_date import UtcDate
from src.domain.village.village_cast import VillageCast
from src.domain.village.village_position import VillagePosition


@dataclass(frozen=True)
class VillageBans:
    position: VillagePosition
    trip: str


@dataclass(frozen=True)
class Village:
    # 村の最小人数 (ここまでしか記録していない)
    MIN_PEOPLE = 8

    # 村の最小人数 (るる鯖の仕様的に 30 人が最大となる)
    MAX_PEOPLE = 30

    village_number: int
    end_date: UtcDate
    name: str
    people: int
    cast: VillageCast
    bans: List[VillageBans]
