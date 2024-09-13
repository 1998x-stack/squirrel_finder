# logger.py

import logging
from config import LOG_FILE

# 配置日志记录器
logging.basicConfig(
    filename=LOG_FILE,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def log_event(event: str):
    """将事件记录到日志文件中。"""
    logging.info(event)