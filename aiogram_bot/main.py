"""The telegram launch module of the bot."""

import asyncio

from aiogram import Bot, Dispatcher

from handlers.routers import register_routers
from loader import bot, dp, on_shutdown, start_up
from utils import logging


async def main(bot: Bot, dp: Dispatcher) -> None:
    """The main function. Launches the bot."""
    dp.startup.register(start_up)
    dp.shutdown.register(on_shutdown)

    register_routers(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main(bot, dp))
