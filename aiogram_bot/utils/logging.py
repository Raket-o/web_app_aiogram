"""The logger module. Writes the log to ./logs/."""

import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler

__DIR_LOGS = "logs"

if not os.path.exists(__DIR_LOGS):
    os.makedirs(__DIR_LOGS)

log_file_handler = TimedRotatingFileHandler(
    filename=f"./{__DIR_LOGS}/loging.log", when="H", interval=10, backupCount=3
)
stream_handler = logging.StreamHandler(stream=sys.stdout)

logging.basicConfig(
    format=(
        "level: %(levelname)s | "
        "logger: %(name)s | "
        "time: %(asctime)s | "
        "line №: %(lineno)s | "
        "message: %(message)s"
    ),
    level=logging.INFO,
    handlers=[stream_handler, log_file_handler],
)
