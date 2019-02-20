import logging
import logging.config
from book_api.modules.ba_logging.log_config import logConfig

logging.config.dictConfig(logConfig)


def get_logger(logger):
    return logging.getLogger(logger)


def close_log(logger):
    handlers = list(logger.handlers)
    for handler in handlers:
        logger.removeHandler(handler)
        handler.flush()
        handler.close()
