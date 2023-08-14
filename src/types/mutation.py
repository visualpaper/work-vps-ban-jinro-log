import strawberry

from src.types.types import User
from src.resolvers.users.users_resolver import initialize as initialize_resolver


@strawberry.type
class Mutation:
    initialize: User = strawberry.field(resolver=initialize_resolver)
