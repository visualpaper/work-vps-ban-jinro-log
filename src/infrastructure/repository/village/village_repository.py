from typing import List

from fastapi import Depends

from src.domain.utc_date import UtcDate
from src.domain.village.village import Village, VillageBans
from src.domain.village.village_cast import VillageCast
from src.domain.village.village_condition import VillageCondition
from src.domain.village.village_position import VillagePosition
from src.domain.village.village_repository import VillageRepository
from src.infrastructure.mongodb.village.village_dao import VillageDao
from src.infrastructure.mongodb.village.village_dto import VillageDto


class VillageRepositoryImpl(VillageRepository):
    def __init__(self, dao: VillageDao = Depends(VillageDao)):
        self._dao = dao

    def _to_model(self, dto: VillageDto) -> Village:
        return Village(
            str(dto["_id"]),
            dto["villageNumber"],
            UtcDate.from_epoch_seconds(dto["endDate"]),
            dto["name"],
            dto["people"],
            VillageCast.of(dto["cast"]),
            [
                VillageBans(VillagePosition.of(ban["position"]), ban["trip"])
                for ban in dto["bans"]
            ],
        )

    def select(self, condition: VillageCondition) -> List[Village]:
        dtos: List[VillageDto] = self._dao.select(condition)

        return [self._to_model(dto) for dto in dtos]
