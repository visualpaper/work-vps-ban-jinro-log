from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class User:
    _id: str
    _village_numbers: List[int]

    @property
    def id(self) -> str:
        return self._id

    @property
    def village_numbers(self) -> List[int]:
        return self._village_numbers
