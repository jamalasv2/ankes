import logging
import os

from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

API_ID = int(os.environ.get("API_ID", "21839531"))
API_HASH = os.environ.get("API_HASH", "2ea72246a26c4c29cc419175f738efa3")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7946571542:AAG8YjxNGjh0blV95VcTTjt5Hmc5ved-pfs")


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
