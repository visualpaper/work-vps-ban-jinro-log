from typing import List

from fastapi import Depends

from src.domain.village.village import Village
from src.domain.village.village_condition import VillageCondition
from src.domain.village.village_repository import VillageRepository
from src.infrastructure.repository.village.village_repository import (
    VillageRepositoryImpl,
)


class VillageFacade:
    def __init__(self, repository: VillageRepository = Depends(VillageRepositoryImpl)):
        self._repository = repository

    def list_villages(self, condition: VillageCondition) -> List[Village]:
        return self._repository.select(condition)
