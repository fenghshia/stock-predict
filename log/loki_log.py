from .log_level import LogLevel
from datetime import datetime
from .call_info import CallInfo
from logging import log


class LokiLog:

    level: LogLevel = None
    log_date: datetime = None
    call_info: CallInfo = None

    def __init__(self, level: LogLevel, call_info: CallInfo):
        self.log_date = datetime.now()
        self.level = level
        self.call_info = call_info

    @property
    def extra(self):
        return dict(
            **self.call_info.call_chain,
            req_id=self.call_info.req_id,
            **self.call_info.start_function,
            **self.call_info.current_function,
            log_date=self.log_date.strftime("%Y-%m-%d %H:%M:%S"),
            level=self.level.name
        )
