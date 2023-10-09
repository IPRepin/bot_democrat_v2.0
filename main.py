import asyncio
import logging
import os
import sys
from dotenv import load_dotenv

from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from aiogram.types import BotCommand

from bot import register_handlers, bot_commands

load_dotenv()


async def run_bot() -> None:

    commands_for_bot = [BotCommand(command=cmd[0], description=cmd[1]) for cmd in bot_commands]
    token = os.getenv("TOKEN")
    dp = Dispatcher()
    bot = Bot(token, parse_mode=ParseMode.HTML)
    await bot.set_my_commands(commands=commands_for_bot)
    # register_handlers(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(run_bot())