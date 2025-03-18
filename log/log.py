from .log_level import *
from .loki_log import LokiLog
from .call_info import CallInfo


class Process(Enum):
    CACHE = 'cache'
    EXTRACT = 'extract'
    DROP = 'drop'


class Log:

    # 日志操作 Cache | Extract | Drop
    process: Process = None
    loki_log: LokiLog = None

    def __init__(self, process: Process, level: LogLevel, call_info: CallInfo):
        self.process = process
        self.loki_log = LokiLog(call_info=call_info, level=level)
