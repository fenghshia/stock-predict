from types import FunctionType
from datetime import datetime
from .call_info import CallInfo


class LokiLog:

    log_date: datetime = None
    call_info: CallInfo = None

    def __init__(self, call_info: CallInfo):
        self.log_date = datetime.now()
        self.call_info = call_info

    @property
    def extra(self):
        return dict(
            **self.call_info.call_chain,
            req_id=self.call_info.req_id,
            **self.call_info.start_function,
            **self.call_info.current_function,
            log_date=self.log_date.strftime("%Y-%m-%d %H:%M:%S")
        )
