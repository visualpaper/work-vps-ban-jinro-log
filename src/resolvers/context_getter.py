from typing import Union

from fastapi import Cookie, Depends

from src.application.user_facade import UserFacade
from src.config.config import Settings, get_config


def get_context(
    sid: Union[str, None] = Cookie(default=None),
    config: Settings = Depends(get_config),
    user_facade: UserFacade = Depends(UserFacade),
):
    return {"sid": sid, "config": config, "user_facade": user_facade}
