from enum import Enum
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL


class LogLevel(Enum):
    DEBUG = DEBUG
    INFO = INFO
    WARNING = WARNING
    ERROR = ERROR
    CRITICAL = CRITICAL


DEBUG = LogLevel.DEBUG
INFO = LogLevel.INFO
WARNING = LogLevel.WARNING
ERROR = LogLevel.ERROR
CRITICAL = LogLevel.CRITICAL
