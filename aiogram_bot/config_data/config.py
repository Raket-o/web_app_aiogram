"""
the config module is used to check whether the environment has been created
"""
import os

from dotenv import find_dotenv, load_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

LOCAL_UTC = os.getenv("LOCAL_UTC")

BOT_TOKEN = os.getenv("BOT_TOKEN")
START_MESSAGE = os.getenv("START_MESSAGE")
ULR_WEB_APP = os.getenv("ULR_WEB_APP")
DEFAULT_MINING_IN_MINUTE = os.getenv("DEFAULT_MINING_IN_MINUTE")
