from typing import Dict, List, Union

import pymongo
from fastapi import Depends
from pymongo.collection import Collection
from pymongo.database import Database

from src.config.mongodb import get_database
from src.domain.village.village_condition import VillageCondition
from src.infrastructure.mongodb.village.village_dto import VillageDto


class VillageDao:
    def __init__(self, db: Database = Depends(get_database)):
        self._collection: Collection = db["td_village"]

    def _create_find(
        self, condition: VillageCondition
    ) -> Dict[str, List[Dict[str, Union[str, int]]]]:
        conditions = []

        if condition.trip is not None:
            conditions.append({"bans": {"$elemMatch": {"trip": condition.trip}}})

        if condition.people_min is not None:
            conditions.append({"people": {"$gte": condition.people_min}})

        if condition.people_max is not None:
            conditions.append({"people": {"$lte": condition.people_max}})

        if len(condition.casts) != 0:
            conditions.append(
                {"cast": {"$in": [cast.value for cast in condition.casts]}}
            )

        if len(condition.positions) != 0:
            conditions.append(
                {
                    "bans": {
                        "$elemMatch": {
                            "position": {
                                "$in": [
                                    position.value for position in condition.positions
                                ]
                            }
                        }
                    }
                }
            )

        if len(conditions) == 0:
            return {}

        return {"$and": conditions}

    def select(self, condition: VillageCondition) -> List[VillageDto]:
        select_find = self._create_find(condition)

        return list(
            self._collection.find(select_find)
            .sort("endDate", pymongo.DESCENDING)
            .skip(condition.skip)
            .limit(condition.take)
        )
