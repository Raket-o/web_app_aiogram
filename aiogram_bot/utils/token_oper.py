"""token processing module"""

import datetime
from datetime import datetime, timedelta, timezone

import jwt
from aiogram_bot.config_data.config import (
    ALGORITHM,
    BOT_TOKEN
)


def create_access_token(data: dict):
    """the token creation function"""
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, BOT_TOKEN, algorithm=ALGORITHM)
    return encoded_jwt
