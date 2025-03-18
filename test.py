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
from log.log_level import *


print(dir(DEBUG))
print(DEBUG.name)
