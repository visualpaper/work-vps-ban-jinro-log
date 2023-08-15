from src.exceptions.ban_jinro_log_exception import BanJinroLogException
from src.logcode import LogCode


class UnauthorizedException(BanJinroLogException):
    def __init__(self):
        super().__init__(LogCode.UNAUTHORIZED)
