from fastapi import Depends

from src.application.adapter.village_result import VillageResult
from src.domain.village.village_condition import VillageCondition
from src.domain.village.village_repository import VillageRepository
from src.infrastructure.repository.village.village_repository import (
    VillageRepositoryImpl,
)


class VillageFacade:
    def __init__(self, repository: VillageRepository = Depends(VillageRepositoryImpl)):
        self._repository = repository

    def list_villages(self, condition: VillageCondition) -> VillageResult:
        return VillageResult(
            totalItems=self._repository.count(condition),
            villages=self._repository.select(condition),
        )
