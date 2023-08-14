from fastapi import Request
from graphql import ExecutionResult, GraphQLError, GraphQLFormattedError
from strawberry.http import GraphQLHTTPResponse
from strawberry.fastapi import GraphQLRouter
from src.logcode import LogCode
from src.config.logger import get_logger


logger = get_logger()


class MyGraphQLRouter(GraphQLRouter):
    async def process_result(
        self, request: Request, result: ExecutionResult
    ) -> GraphQLHTTPResponse:
        data: GraphQLHTTPResponse = {"data": result.data}

        if result.errors:
            data["errors"] = [self._to_error(err) for err in result.errors]

        return data

    def _to_error(self, error: GraphQLError) -> GraphQLFormattedError:
        if error.extensions and hasattr(error.extensions, "code"):
            self._do_logging(
                getattr(error.extensions, "code"),
                getattr(error.extensions, "level"),
                error,
            )
            return {"message": error.message, "extensions": error.extensions}

        # ここから先は結構力技となっている。
        # * code 値がない (基盤例外でない) 場合は、いずれも予期せぬエラーとしている。
        self._do_logging(LogCode.UNEXPECTED.code, LogCode.UNEXPECTED.log_level, error)

        # * error.formatted の中から、message と extensions だけ設定するようにしている。
        formatted: GraphQLFormattedError = {
            "message": error.message or "An unknown error occurred.",
        }
        if error.extensions:
            formatted["extensions"] = error.extensions
        return formatted

    def _do_logging(self, log_code: str, log_level: int, exc: GraphQLError) -> None:
        logger.log(
            level=log_level,
            msg="{} {}".format(log_code, exc.message),
        )
        logger.info("exc", exc_info=exc)
