from typing import Optional

from strawberry.types import Info

from src.application.feedback_facade import FeedbackFacade
from src.types.types import FeedbackInput


def send_feedback(info: Info, input: FeedbackInput) -> Optional[bool]:
    facade: FeedbackFacade = info.context["feedback_facade"]

    facade.feedback(input.name, input.address, input.content)
    return True
