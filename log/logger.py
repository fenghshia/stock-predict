from .log import Log
from .log_level import *
from queue import Queue
from types import FunctionType
from logging import getLogger
from .call_info import CallInfo
from logging_loki import LokiHandler


class Logger:

    handler = LokiHandler(
        url="http://192.168.160.50:3100/loki/api/v1/push",
        tags={"application": "stock-predict"},
        version="2",
    )
    logger = getLogger("stock-predict-logger")
    logger.addHandler(handler)
    logs_cache = dict()
    main_queue = Queue()

    @classmethod
    def log(cls, func: FunctionType):
        def wrapper(*args, call_info: CallInfo = None, **kwargs):
            if call_info is None:
                call_info = CallInfo(func)
            else:
                call_info.add(func)
            log = Log('cache', call_info, "info")
            cls.logger.log(DEBUG)
            print(log.loki_log.extra)
            return func(*args, call_info=call_info, **kwargs)
        return wrapper

    @classmethod
    def __log(cls):
        pass


if __name__ == '__main__':

    @Logger.log
    def x(i):
        print('x')

    x()
