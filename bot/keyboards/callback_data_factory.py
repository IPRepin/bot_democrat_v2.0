"""
Модуль Callback фабрики
"""
from aiogram.filters.callback_data import CallbackData


class StocksCallback(CallbackData, prefix="stocks_callback"):
    stock_name: str
    stock_date: str
