from typing import List

import mongomock
import pytest
from bson import ObjectId
from pymongo.collection import Collection

from src.domain.utc_date import UtcDate
from src.domain.village.village import Village
from src.domain.village.village_cast import VillageCast
from src.domain.village.village_condition import VillageCondition
from src.domain.village.village_position import VillagePosition
from src.infrastructure.mongodb.village.village_dao import VillageDao
from src.infrastructure.mongodb.village.village_dto import VillageBansDto, VillageDto


class TestVillageDao:
    _dao: VillageDao
    _collection: Collection
    DTO_1: VillageDto = VillageDto(
        _id=ObjectId(),
        villageNumber=1,
        endDate=(
            UtcDate.from_timezone_string(
                "2023-10-22T19:34:59Z", "%Y-%m-%dT%H:%M:%SZ"
            ).to_epoch_seconds()
        ),
        name="aaa",
        people=10,
        cast=VillageCast.A.value,
        bans=[VillageBansDto(position=VillagePosition.WOLF.value, trip="aaa")],
    )
    DTO_2: VillageDto = VillageDto(
        _id=ObjectId(),
        villageNumber=2,
        endDate=(
            UtcDate.from_timezone_string(
                "2023-10-23T19:34:59Z", "%Y-%m-%dT%H:%M:%SZ"
            ).to_epoch_seconds()
        ),
        name="bbb",
        people=11,
        cast=VillageCast.A.value,
        bans=[
            VillageBansDto(position=VillagePosition.APOSTATE.value, trip="cc"),
            VillageBansDto(position=VillagePosition.CAT.value, trip="dd"),
        ],
    )
    DTO_3: VillageDto = VillageDto(
        _id=ObjectId(),
        villageNumber=3,
        endDate=(
            UtcDate.from_timezone_string(
                "2023-10-24T19:34:59Z", "%Y-%m-%dT%H:%M:%SZ"
            ).to_epoch_seconds()
        ),
        name="ddd",
        people=16,
        cast=VillageCast.Z.value,
        bans=[
            VillageBansDto(position=VillagePosition.HUNTER.value, trip="rrr"),
            VillageBansDto(position=VillagePosition.CAT.value, trip="dd"),
        ],
    )

    @pytest.fixture(autouse=True)
    def fixture(self):
        client = mongomock.MongoClient()
        db = client["db"]
        self._dao = VillageDao(db)
        self._collection = client["db"]["td_village"]

        # 事前にデータを登録しておく。
        self._collection.insert_many([self.DTO_1, self.DTO_2, self.DTO_3])

        yield
        client.drop_database("db")

    @pytest.mark.parametrize(
        "condition, expected",
        [
            # skip/take 条件
            (VillageCondition.no_condition(3, 1), []),
            (VillageCondition.no_condition(0, 2), [DTO_3, DTO_2]),
            (VillageCondition.no_condition(1, 2), [DTO_2, DTO_1]),
            (VillageCondition.no_condition(1, 1), [DTO_2]),
            # trip 条件
            (
                VillageCondition(
                    "あ", Village.MIN_PEOPLE, Village.MAX_PEOPLE, [], [], 0, 5
                ),
                [],
            ),
            (
                VillageCondition(
                    "rrr", Village.MIN_PEOPLE, Village.MAX_PEOPLE, [], [], 0, 5
                ),
                [DTO_3],
            ),
            (
                VillageCondition(
                    "dd", Village.MIN_PEOPLE, Village.MAX_PEOPLE, [], [], 0, 5
                ),
                [DTO_3, DTO_2],
            ),
            # 人数最小条件
            (VillageCondition(None, 19, Village.MAX_PEOPLE, [], [], 0, 5), []),
            (VillageCondition(None, 12, Village.MAX_PEOPLE, [], [], 0, 5), [DTO_3]),
            (
                VillageCondition(None, 11, Village.MAX_PEOPLE, [], [], 0, 5),
                [DTO_3, DTO_2],
            ),
            # 人数最大条件
            (VillageCondition(None, Village.MIN_PEOPLE, 9, [], [], 0, 5), []),
            (VillageCondition(None, Village.MIN_PEOPLE, 10, [], [], 0, 5), [DTO_1]),
            (
                VillageCondition(None, Village.MIN_PEOPLE, 11, [], [], 0, 5),
                [DTO_2, DTO_1],
            ),
            # cast 条件
            (
                VillageCondition(
                    None,
                    Village.MIN_PEOPLE,
                    Village.MAX_PEOPLE,
                    [VillageCast.B],
                    [],
                    0,
                    5,
                ),
                [],
            ),
            (
                VillageCondition(
                    None,
                    Village.MIN_PEOPLE,
                    Village.MAX_PEOPLE,
                    [VillageCast.Z],
                    [],
                    0,
                    5,
                ),
                [DTO_3],
            ),
            (
                VillageCondition(
                    None,
                    Village.MIN_PEOPLE,
                    Village.MAX_PEOPLE,
                    [VillageCast.A],
                    [],
                    0,
                    5,
                ),
                [DTO_2, DTO_1],
            ),
            (
                VillageCondition(
                    None,
                    Village.MIN_PEOPLE,
                    Village.MAX_PEOPLE,
                    [VillageCast.A, VillageCast.Z],
                    [],
                    0,
                    5,
                ),
                [DTO_3, DTO_2, DTO_1],
            ),
            # position 条件
            (
                VillageCondition(
                    None,
                    Village.MIN_PEOPLE,
                    Village.MAX_PEOPLE,
                    [],
                    [VillagePosition.FOX],
                    0,
                    5,
                ),
                [],
            ),
            (
                VillageCondition(
                    None,
                    Village.MIN_PEOPLE,
                    Village.MAX_PEOPLE,
                    [],
                    [VillagePosition.WOLF],
                    0,
                    5,
                ),
                [DTO_1],
            ),
            (
                VillageCondition(
                    None,
                    Village.MIN_PEOPLE,
                    Village.MAX_PEOPLE,
                    [],
                    [VillagePosition.CAT],
                    0,
                    5,
                ),
                [DTO_3, DTO_2],
            ),
            (
                VillageCondition(
                    None,
                    Village.MIN_PEOPLE,
                    Village.MAX_PEOPLE,
                    [],
                    [VillagePosition.WOLF, VillagePosition.CAT],
                    0,
                    5,
                ),
                [DTO_3, DTO_2, DTO_1],
            ),
            # 複合条件
            (
                VillageCondition(
                    "dd",
                    Village.MIN_PEOPLE,
                    Village.MAX_PEOPLE,
                    [VillageCast.Z],
                    [VillagePosition.HUNTER],
                    0,
                    5,
                ),
                [DTO_3],
            ),
        ],
    )
    def test_select(self, condition: VillageCondition, expected: List[VillageDto]):
        actual: List[VillageDto] = self._dao.select(condition)

        assert len(actual) == len(expected)
        for i in range(len(expected)):
            assert actual[i]["_id"] == expected[i]["_id"]
