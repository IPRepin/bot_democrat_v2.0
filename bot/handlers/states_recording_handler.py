"""
Модуль машины состояний получения данных пользователя
и их передачи в АМО.
"""

import asyncio

from aiogram import types
from aiogram.fsm.context import FSMContext

from amo_integration.amo_commands import add_contact
from bot.keyboards.main_keyboards import main_menu
from bot.misc.states_online_recording import OnlineRecording
from bot.models.db_commands import add_patient
from media_bot.texts import waiting_text


async def enter_name(call: types.CallbackQuery, state: FSMContext):
    """
    Функция получения имени
    пользователя в АМО
    """
    await call.message.answer("Введите имя:")
    await state.set_state(OnlineRecording.NAME)
    await asyncio.sleep(40)
    if await state.get_state() == "OnlineRecording:NAME":
        await call.message.answer(waiting_text, reply_markup=main_menu)
        await state.clear()


async def enter_phone(message: types.Message, state: FSMContext):
    """
    Функция получения номера телефона
    пользователя в АМО
    """
    await state.update_data(answer_name=message.text)
    await message.answer("Введите номер телефона:")
    await state.set_state(OnlineRecording.PHONE)
    await asyncio.sleep(40)
    if await state.get_state() == "OnlineRecording:PHONE":
        await message.answer(waiting_text, reply_markup=main_menu)
        await state.clear()


async def end_enter(message: types.Message, state: FSMContext):
    """
    Функция получения передачи данных
    пользователя в АМО
    """
    data = await state.get_data()
    name = data.get("answer_name")
    phone = message.text
    await message.answer(
        f"Спасибо {name} ваш номер {phone}\n"
        f"Администратор свяжется с вами в течении 10 минут.",
        reply_markup=main_menu,
    )
    await add_patient(user_id=message.from_user.id, name=name, phone=phone)
    await add_contact(name=name, phone=phone)
    await state.clear()
