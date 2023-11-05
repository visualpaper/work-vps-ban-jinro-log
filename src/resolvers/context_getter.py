from typing import Union

from fastapi import Cookie, Depends

from src.application.feedback_facade import FeedbackFacade
from src.application.user_facade import UserFacade
from src.application.village_facade import VillageFacade
from src.config.config import Settings, get_config
from src.resolvers.villages.scheme.villages_scheme import VillagesScheme


def get_context(
    sid: Union[str, None] = Cookie(default=None),
    config: Settings = Depends(get_config),
    user_facade: UserFacade = Depends(UserFacade),
    village_facade: VillageFacade = Depends(VillageFacade),
    villages_scheme: VillagesScheme = Depends(VillagesScheme),
    feedback_facade: FeedbackFacade = Depends(FeedbackFacade),
):
    return {
        "sid": sid,
        "config": config,
        "user_facade": user_facade,
        "village_facade": village_facade,
        "villages_scheme": villages_scheme,
        "feedback_facade": feedback_facade,
    }
