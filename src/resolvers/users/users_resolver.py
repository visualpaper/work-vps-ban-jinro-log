
import strawberry
from strawberry.types import Info
from src.config.mongodb import get_database

from src.config.config import Settings
from src.types.types import User


def initialize(self, info: Info) -> User:
    sid: str = info.context["sid"]
    config: Settings = info.context["config"]
    # db = get_database()
    # print(db["tm_user"].count_documents({}))

    if sid is not None:
        # mongodb から取得
        return User(id=strawberry.ID("aaa"), villageNumbers=[])

    # mongodb に生成
    # cookie 生成
    info.context["response"].set_cookie(
        key=config.cookie_name,
        value="aaa",
        # JavaScript でアクセス不可にする (サーバに送信するだけにする)
        httponly=True,
        # https 通信の時のみ Cookie を利用可能とする
        secure=True,
        # ファーストパーティのコンテキストのみで利用される Cookie とする
        samesite="strict",
        # Cookieの残存期間 (秒数)
        max_age=config.cookie_max_age_seconds,
    )

    return User(id=strawberry.ID("aaa"), villageNumbers=[])
