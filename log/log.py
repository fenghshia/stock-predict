# from typing import Literal
from .loki_log import LokiLog
from .call_info import CallInfo


class Log:

    # 日志操作 Cache | Extract | Drop
    # process: Literal['cache', 'extract', 'drop'] = None
    process = None
    loki_log: LokiLog = None

    # def __init__(self, process: Literal['cache', 'extract', 'drop'], call_info: CallInfo):
    def __init__(self, process, call_info: CallInfo):
        self.process = process
        self.loki_log = LokiLog(call_info=call_info)
