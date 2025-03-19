import traceback
from datetime import datetime
from .call_info import CallInfo, EventInfo
from .log_level import LogLevel


class LokiLog:

    __msg: str = None
    level: LogLevel = None
    log_date: datetime = None
    call_info: CallInfo = None
    event_info: EventInfo = None

    def __init__(self, level: LogLevel, call_info: CallInfo = None, msg: str = None, event_info: EventInfo = None):
        self.log_date = datetime.now()
        self.level = level
        self.call_info = call_info
        self.__msg = msg
        self.event_info = event_info

    @property
    def extra(self) -> dict:
        info = dict(
            log_date=self.log_date.strftime("%Y-%m-%d %H:%M:%S"),
            level=self.level.name
        )
        if self.call_info is not None:
            info.update(
                **self.call_info.call_chain,
                req_id=self.call_info.req_id,
                job_id=self.event_info.job_id,
                **self.call_info.start_function,
                **self.call_info.current_function
            )
        elif self.event_info.exc is not None:
            info.update(
                job_id=self.event_info.job_id,
                traceback=''.join(traceback.format_tb(self.event_info.exc.__traceback__))
            )
        else:
            info.update(job_id=self.event_info.job_id)
        return {"tags": info}

    @property
    def msg(self) -> str:
        if self.call_info is not None:
            return self.__msg
        elif self.event_info.exc is not None:
            return self.event_info.exc.__str__()
        else:
            return "任务 [{}] 执行完成".format(self.event_info.job_id)

    @property
    def job_id(self) -> str:
        if self.call_info is not None:
            return self.call_info.job_id
        else:
            return self.event_info.job_id
