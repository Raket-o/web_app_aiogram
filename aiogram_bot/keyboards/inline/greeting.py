"""The keyboard creation module."""

from aiogram import types

from aiogram.types import InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config_data.config import ULR_WEB_APP
from utils.token_oper import create_access_token


def greeting_buttons(message: types.Message) -> InlineKeyboardMarkup:
    """
    Keyboard creation function.
    :return: InlineKeyboardMarkup
    """
    keyboard_builder = InlineKeyboardBuilder()

    data_for_token = {
        "messanger_id": message.chat.id,
        "messanger": "telegram",
        "first_name": message.chat.first_name,
        "last_name": message.chat.last_name,
    }
    jwt_token = create_access_token(data_for_token)


    # import jwt
    # from jwt.exceptions import InvalidSignatureError
    # from config_data.config import ALGORITHM, BOT_TOKEN
    # payload = jwt.decode(jwt_token, BOT_TOKEN, algorithms=[ALGORITHM])
    # print(type(payload), payload)
    print(ULR_WEB_APP+jwt_token)

    keyboard_builder.button(
        text="Запустить приложение",
        web_app=WebAppInfo(url=ULR_WEB_APP+jwt_token),
    )
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
