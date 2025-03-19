from .log_level import *
from .loki_log import LokiLog
from .call_info import CallInfo, EventInfo


class Process(Enum):

    LOG = 'log'
    CACHE = 'cache'
    EXTRACT = 'extract'
    DROP = 'drop'


LOG = Process.LOG
CACHE = Process.CACHE
EXTRACT = Process.EXTRACT
DROP = Process.DROP


class Log:

    # 日志操作 Log | Cache | Extract | Drop
    process: Process = None
    loki_log: LokiLog = None

    def __init__(self, process: Process, level: LogLevel, call_info: CallInfo = None, msg: str = None, event_info: EventInfo = None):
        self.process = process
        self.loki_log = LokiLog(call_info=call_info, level=level, msg=msg, event_info=event_info)
