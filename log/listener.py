from scheduler import scheduler
from apscheduler.events import *
from .logger import Logger
from .log import *
from .log_level import *
from .call_info import CallInfo


def event_listener(event):
    if event.exception:
        Logger.main_queue.put(
            Log(LOG, ERROR, CallInfo(), msg)
        )
    else:
        Logger.main_queue.put(
            Log(LOG, INFO, CallInfo(), msg)
        )


scheduler.add_listener(event_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
