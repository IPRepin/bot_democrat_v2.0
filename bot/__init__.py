__all__ = ["register_handlers", "bot_commands"]

from aiogram.filters import Command
from aiogram import Router, F

from bot.handlers.main_users_handler import (user_start,
                                             user_help,
                                             stocks,
                                             recording,
                                             story_recording,
                                             taxi,
                                             review_clinic)
from bot.handlers.stocks_handler import osstem_btn, hygiene_btn, brecket_btn

bot_commands = (
    ("start", "Запуск бота", "Начало работа с ботом"),
    ("help", "Что умеет этот бот?", "Помощь при взаимодействии с ботом"),
)


def register_handlers(router: Router) -> None:
    router.message.register(user_start, Command(commands=["start"]))
    router.message.register(user_help, Command(commands=["help"]))
    router.message.register(stocks, F.text == "💫Акции и скидки")
    router.message.register(recording, F.text == "✅Записаться на прием")
    router.message.register(story_recording, F.text == "📑Ваши записи")
    router.message.register(taxi, F.text == "🚕Такси до клиники")
    router.message.register(review_clinic, F.text == "🤩Скидка 5️% за отзыв о клинике")
    router.callback_query.register(osstem_btn, F.data == "osstem")
    router.callback_query.register(hygiene_btn, F.data == "hygiene")
    router.callback_query.register(brecket_btn, F.data == "brecket")
