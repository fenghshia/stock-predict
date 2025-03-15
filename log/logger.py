from queue import Queue
from call_info import CallInfo


class Logger:

    main_queue = Queue()
    logs_cache = dict()

    @classmethod
    def log(cls, func):
        def wrapper(*args, **kwargs):
            call_info = kwargs.get('call_info')
            if call_info is None:
                call_info = CallInfo(func)
            print(type(func))
            print(dir(func))
            print(dir(func.__code__))
            print(func.__name__)
            print(func.__code__.co_filename)
            print(func.__code__.co_firstlineno)
            print(args)
            return func(*args, **kwargs, call_info=call_info)
        return wrapper

    @classmethod
    def __log(cls):
        pass


if __name__ == '__main__':

    @Logger.log
    def x(i):
        print('x')

    x(87)
