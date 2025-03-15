from typing import Literal


class Log:

    # 日志操作 Cache | Extract | Drop
    process = None
    loki_log = None

    def __init__(self,
                 process: Literal['cache', 'extract', 'drop']):
        self.process = process


class LokiLog:

    start_function = None
