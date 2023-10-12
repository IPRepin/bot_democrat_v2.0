"""
Функции обработки кнопок списка акций
"""
import logging

from aiogram import types

from bot.keyboards.main_keyboards import main_menu
from bot.keyboards.stocks_keyboards import (osstem_keyboard,
                                            hygiene_keyboard,
                                            brecket_keyboard)
from bot.models.db_commands import select_stock


async def osstem_btn(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    stock = await select_stock(1)
    await call.message.answer_photo(
        stock.stock_image,
        caption=f"{stock.stock_name}\n" f"{stock.stock_description}",
        reply_markup=osstem_keyboard,
    )


async def hygiene_btn(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    stock = await select_stock(2)
    await call.message.answer_photo(
        stock.stock_image,
        caption=f"{stock.stock_name}\n" f"{stock.stock_description}",
        reply_markup=hygiene_keyboard,
    )


async def brecket_btn(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    stock = await select_stock(3)
    await call.message.answer_photo(
        stock.stock_image,
        caption=f"{stock.stock_name}\n" f"{stock.stock_description}",
        reply_markup=brecket_keyboard,
    )


async def cancel_btn(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Главное меню: ", reply_markup=main_menu)