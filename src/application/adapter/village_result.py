from dataclasses import dataclass
from typing import List

from src.domain.village.village import Village


@dataclass(frozen=True)
class VillageResult:
    totalItems: int
    villages: List[Village]
