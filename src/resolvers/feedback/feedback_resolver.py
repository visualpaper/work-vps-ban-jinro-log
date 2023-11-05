from typing import Optional

from strawberry.types import Info

from src.application.feedback_facade import FeedbackFacade
from src.exceptions.exceptions import BadRequestException
from src.types.types import FeedbackInput


def send_feedback(info: Info, input: FeedbackInput) -> Optional[bool]:
    sid: str = info.context["sid"]
    facade: FeedbackFacade = info.context["feedback_facade"]

    if sid is None:
        raise BadRequestException()

    facade.feedback(input.name, input.address, input.content)
    return True
