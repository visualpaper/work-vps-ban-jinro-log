from typing import Optional

import strawberry
from strawberry.types import Info

from src.application.user_facade import UserFacade
from src.config.config import Settings
from src.domain.user import User
from src.types.types import UserSchema


def initialize(info: Info) -> UserSchema:
    sid: str = info.context["sid"]
    config: Settings = info.context["config"]
    facade: UserFacade = info.context["user_facade"]

    # SessionId が存在している場合は該当する User を取得し返却する。
    if sid is not None:
        user: Optional[User] = facade.get_user(sid)
        if user is not None:
            return UserSchema(
                id=strawberry.ID(user.id), villageNumbers=user.village_numbers
            )

    # 存在していない場合は 1 時間有効期限で作成し Cookie 上に Session を持たせる。
    created_user: User = facade.create_user()

    info.context["response"].set_cookie(
        key=config.cookie_name,
        value=created_user.id,
        # JavaScript でアクセス不可にする (サーバに送信するだけにする)
        httponly=True,
        # https 通信の時のみ Cookie を利用可能とする
        secure=True,
        # ファーストパーティのコンテキストのみで利用される Cookie とする
        samesite="strict",
        # Cookieの残存期間 (秒数)
        max_age=config.cookie_max_age_seconds,
    )
    return UserSchema(
        id=strawberry.ID(created_user.id), villageNumbers=created_user.village_numbers
    )
