"""User Handler registration module."""

from aiogram import F, Router
from aiogram.filters import Command, CommandStart

from handlers.default_heandlers.start import start_command


def register_routers(router: Router):
    """
    The register_routers function. Collects handlers in the main router.
    """
    router.message.register(start_command, CommandStart())
    router.callback_query.register(
        start_command,
        F.data.startswith("start_command=")
    )
