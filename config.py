import logging
import os

from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", ""))
BOT_TOKEN = os.environ.get("BOT_TOKEN", ""))


