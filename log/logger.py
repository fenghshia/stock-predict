from .log import *
from .log_level import *
from queue import Queue
from types import FunctionType
from logging import getLogger
from logging_loki import LokiHandler


class Logger:

    handler = LokiHandler(
        url="http://192.168.160.50:3100/loki/api/v1/push",
        tags={"application": "stock-predict"},
        version="2",
    )
    logger = getLogger("stock-predict-logger")
    log_level = LogLevel.DEBUG
    logs_cache = dict()
    main_queue = Queue()
    logger.addHandler(handler)

    @classmethod
    def log(cls, func: FunctionType):
        def wrapper(*args, job_id: str = None, call_info: CallInfo = None, **kwargs):
            if call_info is None:
                if job_id is None:
                    raise JobIDIsNone()
                call_info = CallInfo(job_id, func)
            else:
                call_info.add(func)
            cls.__log(DEBUG, call_info, "Function [{}] 被调用".format(func.__name__))
            # cls.logger.log(DEBUG)
            # print(log.loki_log.extra)
            return func(*args, call_info=call_info, log=cls.__log, **kwargs)
        return wrapper

    @classmethod
    def __log(cls, level: LogLevel, call_info: CallInfo, msg: str):
        if level >= cls.log_level:
            cls.main_queue.put(
                Log(LOG, level, call_info, msg)
            )
        else:
            cls.main_queue.put(
                Log(CACHE, level, call_info, msg)
            )


class JobIDIsNone(Exception):

    def __str__(self):
        return '初始化 CallInfo 失败, 未传入job_id'


if __name__ == '__main__':

    @Logger.log
    def x(i):
        print('x')

    x()
