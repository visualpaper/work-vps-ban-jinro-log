from fastapi import Depends

from src.domain.feedback.feedback_repository import FeedbackRepository
from src.infrastructure.repository.feedback.feedback_repository import (
    FeedbackRepositoryImpl,
)


class FeedbackFacade:
    def __init__(
        self, repository: FeedbackRepository = Depends(FeedbackRepositoryImpl)
    ):
        self._repository = repository

    def feedback(self, name: str, address: str, content: str) -> bool:
        self._repository.create(name, address, content)

        return True
