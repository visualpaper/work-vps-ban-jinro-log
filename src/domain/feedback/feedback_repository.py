from abc import ABC, abstractmethod


class FeedbackRepository(ABC):
    @abstractmethod
    def create(self, name: str, address: str, content: str) -> None:
        pass
