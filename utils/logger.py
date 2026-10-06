import logging
from pathlib import Path


log_file = Path("logs/automation.log")
log_file.parent.mkdir(exist_ok=True)

logger = logging.getLogger("automation")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)