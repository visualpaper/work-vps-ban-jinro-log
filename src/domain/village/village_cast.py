from enum import Enum

from src.exceptions.ban_jinro_log_exception import IllegalArgumentsException


class VillageCast(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    Z = "Z"

    @classmethod
    def of(cls, value):
        for t in VillageCast:
            if t.value == value:
                return t

        raise IllegalArgumentsException()