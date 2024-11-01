"""The keyboard creation module."""

from aiogram.types import InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config_data.config import ULR_WEB_APP



def greeting_buttons() -> InlineKeyboardMarkup:
    """
    Keyboard creation function.
    :return: InlineKeyboardMarkup
    """
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(
        text="Запустить приложение",
        web_app=WebAppInfo(url=ULR_WEB_APP)
    )
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
