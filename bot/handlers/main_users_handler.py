from aiogram import types

from bot.keyboards.main_keyboards import main_menu
from media_bot.stickers import sticker_start, sticker_help
from media_bot.texts import text_user_start

"""Функция обработчик кнопки старт"""


async def user_start(message: types.Message) -> None:
    sticker_id = sticker_start
    await message.answer_sticker(sticker=sticker_id)
    await message.answer(
        f"Привет {message.from_user.first_name}," f" {text_user_start}",
        reply_markup=main_menu.as_markup(resize_keyboard=True),
    )


"""Функция обработчик кнопки help"""


async def user_help(message: types.Message):
    sticker_id = sticker_help
    await message.answer_sticker(sticker=sticker_id)
    await message.answer(
        f"Привет {message.from_user.first_name}," f" {text_user_start}",
        reply_markup=main_menu.as_markup(resize_keyboard=True),
    )


"""Функции обработки кнопок основного меню"""
"""Обработчик кнопки Акции и скидки"""


async def stocks(message: types.Message):
    # await message.answer(text_stocks, reply_markup=stocks_keyboard)
    pass

"""Обработчик кнопки ✅Записаться на прием"""


async def recording(message: types.Message):
    # await message.answer(
    #     f"{message.from_user.first_name}\n" f"{text_recording}",
    #     reply_markup=online_entries_keyboard,
    # )
    pass


"""Обработчик кнопки Мои записи"""


async def story_recording(message: types.Message):
    # phone = await select_patient(message.from_user.id)
    # if phone:
    #     msg = info(phone)
    #     await message.answer(msg, reply_markup=not_entries_keyboard)
    # else:
    #     await message.answer(
    #         f"{message.from_user.first_name}\n" f"{text_story_recording}",
    #         reply_markup=not_entries_keyboard,
    #     )
    pass


"""Обработчик кнопки вызова такси"""


async def taxi(message: types.Message):
    # await message.answer(
    #     f"{message.from_user.first_name}\n" f"{text_taxi}", reply_markup=taxi_keyboard
    # )
    pass


"""Обработчик кнопки 🤩Скидка 5️% за отзыв о клинике"""


async def review_clinic(message: types.Message):
    # await message.answer(
    #     f"{message.from_user.first_name}\n" f"{text_discount}",
    #     reply_markup=review_clinic_keyboard,
    # )
    pass