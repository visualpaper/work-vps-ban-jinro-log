import logging

from enum import Enum


class CaseCode(Enum):
    WEB = "WEBC"
    BASE = "BASE"
    STORAGE = "STRG"


class LogCode(Enum):
    # Request Related LogCode.
    BAD_REQUEST = (CaseCode.WEB, 0, logging.INFO, "Bad Request")
    UNAUTHORIZED = (CaseCode.WEB, 1, logging.INFO, "Unauthorized")
    RESOURCE_NOT_FOUND = (CaseCode.WEB, 2, logging.INFO, "Not Found")
    TOO_MANY_REQUESTS = (CaseCode.WEB, 3, logging.INFO, "Too Many Requests")

    # Common Related LogCode.
    UNEXPECTED = (CaseCode.BASE, 0, logging.ERROR, "Unexpected Error")
    ILLEGAL_ARGUMENTS = (CaseCode.BASE, 1, logging.ERROR, "Illegal Arguments")
    IO_ERROR = (CaseCode.BASE, 2, logging.ERROR, "IO Error")

    # Storage Related LogCode.
    STORAGE_UNEXPECTED = (
        CaseCode.STORAGE,
        0,
        logging.ERROR,
        "Storage Unexpected Error",
    )

    def __init__(
        self, case_code: CaseCode, detail_code: int, log_level: int, message: str
    ):
        self._case_code = case_code
        self._detail_code = detail_code
        self._log_level = log_level
        self._message = message

    @property
    def code(self) -> str:
        return "{}-{}".format(self._case_code.value, str(self._detail_code).zfill(4))

    @property
    def log_level(self) -> int:
        return self._log_level

    @property
    def message(self) -> str:
        return self._message
