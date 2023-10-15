from aiogram import types

from amo_integration.amo_commands import info
from bot.keyboards.entries_keyboard import not_entries_keyboard
from bot.keyboards.main_keyboards import main_menu
from bot.keyboards.online_entries_keyboard import online_entries_keyboard
from bot.keyboards.review_clinic_keyboard import review_clinic_keyboard
from bot.keyboards.stocks_keyboards import stocks_keyboard
from bot.keyboards.taxi_keyboard_main import taxi_keyboard
from bot.models.db_commands import add_user, select_patient
from media_bot.stickers import sticker_start, sticker_help
from media_bot.texts import (text_user_start,
                             text_stocks,
                             text_recording,
                             text_taxi,
                             text_discount,
                             text_story_recording,
                             )


async def user_start(message: types.Message) -> None:
    """
    Функция обработчик кнопки старт
    """
    await add_user(
        user_id=message.from_user.id,
        full_name=message.from_user.full_name,
        username=message.from_user.username,
        url=message.from_user.url,
    )
    sticker_id = sticker_start
    await message.answer_sticker(sticker=sticker_id)
    await message.answer(
        f"Привет {message.from_user.first_name}," f" {text_user_start}",
        reply_markup=main_menu,
    )


async def user_help(message: types.Message) -> None:
    """
    Функция обработчик кнопки help
    """
    sticker_id = sticker_help
    await message.answer_sticker(sticker=sticker_id)
    await message.answer(
        f"Привет {message.from_user.first_name}," f" {text_user_start}",
        reply_markup=main_menu,
    )


"""Функции обработки кнопок основного меню"""


async def stocks(message: types.Message):
    """
    Обработчик кнопки Акции и скидки
    """
    await message.answer(text_stocks, reply_markup=stocks_keyboard)


async def recording(message: types.Message) -> None:
    """
    Обработчик кнопки ✅Записаться на прием
    """
    await message.answer(
        f"{message.from_user.first_name}\n" f"{text_recording}",
        reply_markup=online_entries_keyboard,
    )


async def story_recording(message: types.Message) -> None:
    """
    Обработчик кнопки Мои записи
    """
    phone = await select_patient(message.from_user.id)
    if phone:
        msg = info(phone)
        await message.answer(msg, reply_markup=not_entries_keyboard)
    else:
        await message.answer(
            f"{message.from_user.first_name}\n" f"{text_story_recording}",
            reply_markup=not_entries_keyboard,
        )


async def taxi(message: types.Message) -> None:
    """
    Обработчик кнопки вызова такси
    """
    await message.answer(
        f"{message.from_user.first_name}\n" f"{text_taxi}", reply_markup=taxi_keyboard
    )


async def review_clinic(message: types.Message) -> None:
    """
    Обработчик кнопки 🤩Скидка 5️% за отзыв о клинике
    """
    await message.answer(
        f"{message.from_user.first_name}\n" f"{text_discount}",
        reply_markup=review_clinic_keyboard,
    )
