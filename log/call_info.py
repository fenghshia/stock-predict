from uuid import uuid4
from types import FunctionType


class CallInfo:

    __req_id = None
    __call_chain = None

    def __init__(self, func: FunctionType):
        self.__req_id = uuid4()
        self.__call_chain = [func]

    @property
    def req_id(self):
        return self.__req_id.__str__()

    @property
    def start_function(self) -> dict:
        return {"start_function": self.__call_chain[0].__name__}

    @property
    def current_function(self) -> dict:
        return {"current_function": self.__call_chain[0].__name__}

    @property
    def call_chain(self) -> dict:
        call_chain = {"chain": ""}
        for func in self.__call_chain:
            call_chain["chain"] += ">> {}".format(func.__name__)
            call_chain[func.__name__] = "{}:{}".format(func.__code__.co_filename, func.__code__.co_firstlineno)
        return call_chain

    def add(self, func: FunctionType):
        self.__call_chain.append(func)


if __name__ == '__main__':
    print(CallInfo().req_id)
