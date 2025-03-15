from types import FunctionType
from uuid import uuid4


class CallInfo:

    __req_id = None
    __start_function = None

    def __init__(self, func: FunctionType):
        self.__req_id = uuid4()
        self.__start_function = func

    @property
    def req_id(self):
        return self.__req_id.__str__()


if __name__ == '__main__':
    print(CallInfo().req_id)
