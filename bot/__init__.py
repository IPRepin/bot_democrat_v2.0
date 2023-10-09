__all__ = ["register_handlers", "bot_commands"]

from aiogram.filters import Command
from aiogram import Router, F

bot_commands = (
    ("start", "Запуск бота", "Начало работа с ботом"),
    ("help", "Что умеет этот бот?", "Помощь при взаимодействии с ботом"),
)


def register_handlers(router: Router) -> None:
    # router.message.register(start_command, Command(commands=["start"]))
    ...
