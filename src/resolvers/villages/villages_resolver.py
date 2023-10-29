from typing import List

from strawberry.types import Info

from src.types.types import Village, VillagesInput


def list_villages(info: Info, input: VillagesInput) -> List[Village]:
    print(input.skip)
    print(input.take)
    return []
