# import logging
# import logging_loki
#
#
# handler = logging_loki.LokiHandler(
#     url="http://192.168.160.50:3100/loki/api/v1/push",
#     tags={"application": "stock-predict"},
#     version="2",
# )
#
# logger = logging.getLogger("stock-predict-logger")
# logger.addHandler(handler)
# logger.error(
#     "Something happened",
#     extra={"tags": {"service": "my-service"}},
# )
import traceback
from log import *
from datetime import datetime


@scheduler.task('date', run_date=datetime.now())
@Logger.log
def rais_error():
    print(1)


scheduler.start()
log = Logger.main_queue.get()
print(log.loki_log.extra)
print(log.loki_log.msg)

