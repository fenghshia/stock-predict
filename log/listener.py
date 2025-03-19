from .log import *
from .logger import Logger
from .log_level import *
from .call_info import EventInfo


def event_listener(event):
    if event.exception:
        Logger.main_queue.put(
            Log(EXTRACT, ERROR, event_info=EventInfo(event.job_id, event.exception))
        )
    else:
        Logger.main_queue.put(
            Log(DROP, INFO, event_info=EventInfo(event.job_id))
        )
