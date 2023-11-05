from typing import Optional

import strawberry

from src.resolvers.feedback.feedback_resolver import send_feedback
from src.resolvers.users.users_resolver import initialize as initialize_resolver
from src.types.types import UserSchema


@strawberry.type
class Mutation:
    initialize: UserSchema = strawberry.field(resolver=initialize_resolver)
    sendFeedback: Optional[bool] = strawberry.field(resolver=send_feedback)
