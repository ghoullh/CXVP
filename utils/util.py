import logging
import sys
from logging.handlers import RotatingFileHandler

LOGGING_FORMAT = "[%(asctime)s] %(threadName)s %(levelname)s in %(module)s: %(message)s"

FILE_HANDLER = RotatingFileHandler(filename="SVXP.log",
                                   maxBytes=1024 * 1024 * 10, backupCount=10,
                                   mode='a', encoding='utf-8', delay=True)
FILE_HANDLER.setLevel(level=logging.DEBUG)
FILE_HANDLER.setFormatter(logging.Formatter(LOGGING_FORMAT))
STDOUT_HANDLER = logging.StreamHandler(sys.stdout)
STDOUT_HANDLER.setFormatter(logging.Formatter(LOGGING_FORMAT))


def get_logger(name):
    """
    获取和flask server一致格式的logger
    :param name:
    :return:
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(FILE_HANDLER)
    logger.addHandler(STDOUT_HANDLER)
    return logger

