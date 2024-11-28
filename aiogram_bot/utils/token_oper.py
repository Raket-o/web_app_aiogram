"""token processing module"""

import datetime
from datetime import datetime, timedelta, timezone

import jwt
from aiogram_bot.config_data.config import (
    # ACCESS_TOKEN_EXPIRE_MINUTES,
    ALGORITHM,
    BOT_TOKEN
)


# def create_access_token(data: dict, expires_delta: timedelta | None = None):
def create_access_token(data: dict):
    """the token creation function"""
    to_encode = data.copy()
    # if expires_delta:
    #     expire = datetime.now(timezone.utc) + expires_delta
    # else:
    #     expire = datetime.now() + timedelta(
    #         minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    #     )
    # to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, BOT_TOKEN, algorithm=ALGORITHM)
    return encoded_jwt
