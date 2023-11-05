from fastapi import Depends
from pymongo.collection import Collection
from pymongo.database import Database

from src.config.mongodb import get_database
from src.infrastructure.mongodb.feedback.feedback_dto import FeedbackDto


class FeedbackDao:
    def __init__(self, db: Database = Depends(get_database)):
        self._collection: Collection = db["td_feedback"]

    def insert_one(self, dto: FeedbackDto):
        self._collection.insert_one(dto)
