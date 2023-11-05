from bson import ObjectId
from fastapi import Depends

from src.domain.feedback.feedback_repository import FeedbackRepository
from src.infrastructure.mongodb.feedback.feedback_dao import FeedbackDao
from src.infrastructure.mongodb.feedback.feedback_dto import FeedbackDto


class FeedbackRepositoryImpl(FeedbackRepository):
    def __init__(self, dao: FeedbackDao = Depends(FeedbackDao)):
        self._dao = dao

    def create(self, name: str, address: str, content: str) -> None:
        dto: FeedbackDto = FeedbackDto(
            _id=ObjectId(), name=name, address=address, content=content
        )

        self._dao.insert_one(dto)
