import strawberry

from src.resolvers.villages.villages_resolver import list_villages
from src.types.types import VillageResult


@strawberry.type
class Query:
    villages: VillageResult = strawberry.field(resolver=list_villages)
