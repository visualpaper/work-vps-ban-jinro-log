from typing import List

from strawberry.types import Info

from src.application.village_facade import VillageFacade
from src.domain.village.village import Village
from src.domain.village.village_cast import VillageCast
from src.domain.village.village_condition import VillageCondition
from src.domain.village.village_position import VillagePosition
from src.resolvers.villages.scheme.villages_scheme import VillagesScheme
from src.types.types import Village as VillageScheme
from src.types.types import VillagesInput


def list_villages(info: Info, input: VillagesInput) -> List[VillageScheme]:
    facade: VillageFacade = info.context["village_facade"]
    scheme: VillagesScheme = info.context["villages_scheme"]
    condition: VillageCondition = VillageCondition(
        trip=input.trip,
        people_min=input.people_min,
        people_max=input.people_max,
        casts=[VillageCast.of(cast.value) for cast in input.cast],
        positions=[VillagePosition.of(position.value) for position in input.position],
        skip=input.skip,
        take=input.take,
    )

    villages: List[Village] = facade.list_villages(condition)
    return [scheme.to_scheme(village) for village in villages]
