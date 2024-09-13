# logger.py

import logging
from config import LOG_FILE

# Configure the logger
logging.basicConfig(
    filename=LOG_FILE,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def log_event(event: str):
    """Logs an event to the log file."""
    logging.info(event)