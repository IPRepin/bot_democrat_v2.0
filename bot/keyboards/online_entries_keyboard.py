"""
Клавиатура записи пользователя
"""

from aiogram.utils.keyboard import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

online_entries_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🌐Онлайн запись", callback_data="rec_online")],
        [
            InlineKeyboardButton(
                text="📲Связаться через телеграм",
                url="https://t.me/+79302077377",
            )
        ],
        [InlineKeyboardButton(text="↩️На главное меню", callback_data="cancel")],
    ]
)
