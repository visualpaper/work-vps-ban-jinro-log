from abc import ABC, abstractmethod
from typing import List

from src.domain.village.village import Village
from src.domain.village.village_condition import VillageCondition


class VillageRepository(ABC):
    @abstractmethod
    def count(self, condition: VillageCondition) -> int:
        pass

    @abstractmethod
    def select(self, condition: VillageCondition) -> List[Village]:
        pass
