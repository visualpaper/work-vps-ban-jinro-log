import strawberry

from src.resolvers.users.users_resolver import initialize as initialize_resolver
from src.types.types import User


@strawberry.type
class Mutation:
    initialize: User = strawberry.field(resolver=initialize_resolver)
