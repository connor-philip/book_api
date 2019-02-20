import os
from datetime import date

CURRENTFILEPATH = os.path.dirname(os.path.realpath(__file__))
DATETODAY = date.today()
DEFAULTLOGFILENAME = "{}.log".format(DATETODAY)
DEFAULTLOGPATH = os.path.join(CURRENTFILEPATH, DEFAULTLOGFILENAME)

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
            "filename": DEFAULTLOGPATH,
            "class": "logging.FileHandler",
        },
        "databaseModuleHandler": {
            "formatter": "standard",
            "filename": os.path.join(CURRENTFILEPATH, "book_api_database_{}".format(DEFAULTLOGFILENAME)),
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
