"""
Модуль определения состояний для машины состояний онлайн записи
"""
from aiogram.fsm.state import StatesGroup, State


class OnlineRecording(StatesGroup):
    NAME = State()
    PHONE = State()
