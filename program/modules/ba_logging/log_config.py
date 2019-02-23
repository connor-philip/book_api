import os
from datetime import date

LOGBASEPATH = os.environ['book_api_logs']
DEFAULTLOGFILENAME = "{}.log".format(date.today())
DEFAULTLOGFILEPATH = os.path.join(LOGBASEPATH, DEFAULTLOGFILENAME)

if os.path.exists(LOGBASEPATH) is False:
    os.mkdir(LOGBASEPATH)


logConfig = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "datefmt": "%H:%M:%S",
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s - FROM: %(filename)s line:%(lineno)d"
        },
    },
    "handlers": {
        "default": {
            "formatter": "standard",
            "filename": DEFAULTLOGFILEPATH,
            "class": "logging.FileHandler",
        },
        "databaseModuleHandler": {
            "formatter": "standard",
            "filename": os.path.join(LOGBASEPATH, "ba_database_{}".format(DEFAULTLOGFILENAME)),
            "class": "logging.FileHandler",
        }
    },
    "loggers": {
        "databaseModuleLogger": {
            "handlers": ["databaseModuleHandler"],
            "level": "WARNING"
        }
    }
}
