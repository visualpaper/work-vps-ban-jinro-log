from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class User:
    _id: str
    _villageNumbers: List[int]

    @property
    def id(self) -> str:
        return self._id

    @property
    def villageNumbers(self) -> List[int]:
        return self._villageNumbers
