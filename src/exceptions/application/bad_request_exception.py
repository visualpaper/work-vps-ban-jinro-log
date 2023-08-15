from src.exceptions.ban_jinro_log_exception import BanJinroLogException
from src.logcode import LogCode


class BadRequestException(BanJinroLogException):
    def __init__(self):
        super().__init__(LogCode.BAD_REQUEST)
