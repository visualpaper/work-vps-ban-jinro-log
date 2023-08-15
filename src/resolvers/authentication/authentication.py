from typing import Optional, Union

from fastapi import Cookie, Request

from src.exceptions.application.unauthorized_exception import UnauthorizedException


class Authentication:
    def __init__(self, validate: bool = True):
        self._validate = validate

    def __call__(
        self, request: Request, sid: Union[str, None] = Cookie(default=None)
    ) -> Optional[str]:
        if sid is None and self._validate:
            raise UnauthorizedException()

        return sid
