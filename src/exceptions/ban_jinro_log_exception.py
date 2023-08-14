from typing import Optional

from graphql import GraphQLError
from src.logcode import LogCode


# Handler が使いにくい都合上、
# GraphQLError を継承することで GraphQLRouter.process_result にてハンドリングできるようにしている。
class BanJinroLogException(GraphQLError):
    def __init__(self, log_code: LogCode, message: Optional[str] = None):
        super().__init__(
            message=(message if message is not None else log_code.message),
            extensions={"code": log_code.code},
        )
        self._log_code = log_code

    @property
    def log_code(self) -> LogCode:
        return self._log_code
