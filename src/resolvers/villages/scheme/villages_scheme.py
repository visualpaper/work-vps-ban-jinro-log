from zoneinfo import ZoneInfo

import strawberry
from fastapi import Depends

from src.domain.village.village import Village, VillageBans
from src.domain.village.village_cast import VillageCast
from src.domain.village.village_position import VillagePosition
from src.exceptions.exceptions import IllegalArgumentsException
from src.types.types import Village as VillageScheme
from src.types.types import VillageBans as VillageBansScheme
from src.types.types import VillageCast as VillageSchemeCast
from src.types.types import VillagePosition as VillageSchemePosition


class RuruApiUrlFactory:
    URL: str = "https://ruru-jinro.net/log{log_number}/log{number}.html"

    # 1000 ～ 99999 までは log/log99999
    # 100000 ～ 199999 までは log2/log199999
    # 200000 ～ 299999 までは log3/log299999
    # ... のように続いていく。
    SEPARATE_NUMBER: int = 100000

    def create(self, village_number: int) -> str:
        return self.URL.format(
            log_number=self._to_log_number(village_number),
            number=village_number,
        )

    def _to_log_number(self, village_number: int) -> str:
        if village_number < self.SEPARATE_NUMBER:
            return ""

        return str((village_number // self.SEPARATE_NUMBER) + 1)


class VillagesScheme:
    def __init__(self, url_factory: RuruApiUrlFactory = Depends(RuruApiUrlFactory)):
        self._url_factory = url_factory

    def _to_scheme_cast(self, cast: VillageCast) -> VillageSchemeCast:
        if cast == VillageCast.A:
            return VillageSchemeCast.A

        if cast == VillageCast.B:
            return VillageSchemeCast.B

        if cast == VillageCast.C:
            return VillageSchemeCast.C

        if cast == VillageCast.D:
            return VillageSchemeCast.D

        if cast == VillageCast.Z:
            return VillageSchemeCast.Z

        raise IllegalArgumentsException(cast.value)

    def _to_scheme_position(self, position: VillagePosition) -> VillageSchemePosition:
        if position == VillagePosition.WOLF:
            return VillageSchemePosition.WOLF

        if position == VillagePosition.FANATIC:
            return VillageSchemePosition.FANATIC

        if position == VillagePosition.MADMAN:
            return VillageSchemePosition.MADMAN

        if position == VillagePosition.FOX:
            return VillageSchemePosition.FOX

        if position == VillagePosition.APOSTATE:
            return VillageSchemePosition.APOSTATE

        if position == VillagePosition.SEER:
            return VillageSchemePosition.SEER

        if position == VillagePosition.MEDIUM:
            return VillageSchemePosition.MEDIUM

        if position == VillagePosition.HUNTER:
            return VillageSchemePosition.HUNTER

        if position == VillagePosition.CAT:
            return VillageSchemePosition.CAT

        if position == VillagePosition.MASON:
            return VillageSchemePosition.MASON

        if position == VillagePosition.VILLAGER:
            return VillageSchemePosition.VILLAGER

        raise IllegalArgumentsException(position.value)

    def _to_scheme_ban(self, ban: VillageBans) -> VillageBansScheme:
        return VillageBansScheme(
            position=self._to_scheme_position(ban.position), trip=ban.trip
        )

    def to_scheme(self, village: Village) -> VillageScheme:
        return VillageScheme(
            id=strawberry.ID(village.id),
            number=village.village_number,
            endDate=village.end_date.iso_format(ZoneInfo("Asia/Tokyo")),
            url=self._url_factory.create(village.village_number),
            name=village.name,
            people=village.people,
            cast=self._to_scheme_cast(village.cast),
            bans=[self._to_scheme_ban(ban) for ban in village.bans],
        )
