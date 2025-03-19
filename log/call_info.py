from uuid import uuid4, UUID
from types import FunctionType


class EventInfo:

    exc: Exception = None
    job_id: str = None

    def __init__(self, job_id: str, exc: Exception = None):
        self.job_id = job_id
        self.exc = exc


class CallInfo(EventInfo):

    __req_id: UUID = None
    __call_chain = None

    def __init__(self, job_id: str, func: FunctionType):
        super().__init__(job_id)
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
