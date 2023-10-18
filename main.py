import os
import sys

from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis


async def run_bot() -> None:
    commands_for_bot = [BotCommand(command=cmd[0], description=cmd[1]) for cmd in bot_commands]
    host_redis = os.getenv("HOST_REDIS")
    port_redis = int(os.getenv("REDIS_PORT"))
    redis = Redis(host=host_redis, port=port_redis)
    storage = RedisStorage(redis=redis) if os.getenv("USE_REDIS") == True else MemoryStorage()
    token = os.getenv("TOKEN")
    dp = Dispatcher(storage=storage)
    bot = Bot(token, parse_mode=ParseMode.HTML)
    await bot.set_my_commands(commands=commands_for_bot)
    register_handlers(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    import django

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "admin_bot_django.admin_bot_django.settings"
    )
    os.environ.update({'DJANGO_ALLOW_ASYNC_UNSAFE': "true"})
    django.setup()

    import asyncio

    from aiogram import Dispatcher, Bot
    from aiogram.enums import ParseMode
    from aiogram.types import BotCommand

    import logging

    from dotenv import load_dotenv

    from bot import register_handlers, bot_commands

    load_dotenv()
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(run_bot())
