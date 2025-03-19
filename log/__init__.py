# --*-- Coding : UTF-8     --*--
# @Project     : stock-predict
# @File        : __init__.py.py
# @Time        : 2025/2/25 下午4:32
# @IDE         : PyCharm
# @Description : Input Here
# --*-- Author : FengHShia --*--
from .log import Log, LOG, CACHE, EXTRACT, DROP
from .logger import Logger
from .loki_log import LokiLog
from scheduler import scheduler
from .listener import event_listener
from .call_info import EventInfo, CallInfo
from .log_level import LogLevel, DEBUG, INFO, WARNING, ERROR, CRITICAL
from apscheduler.events import *


scheduler.add_listener(event_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
