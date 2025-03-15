from apscheduler.events import *
from scheduler import scheduler


def event_listener(event):
    if event.exception:
        print('The job crashed :(')
    else:
        print('The job worked :)')


scheduler.add_listener(event_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
