from typing import List

import strawberry

from src.resolvers.villages.villages_resolver import list_villages
from src.types.types import Village


@strawberry.type
class Query:
    villages: List[Village] = strawberry.field(resolver=list_villages)
