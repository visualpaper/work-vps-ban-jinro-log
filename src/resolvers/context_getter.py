from typing import Union

from fastapi import Cookie, Depends

from src.config.config import Settings, get_config


def get_context(
    sid: Union[str, None] = Cookie(default=None), config: Settings = Depends(get_config)
):
    return {"sid": sid, "config": config}
