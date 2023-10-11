"""
Клавиатура списка акций
"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

stocks_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🦷Имплантация Osstem от 1200 рублей в месяц",
                callback_data="osstem"
            )
        ],
        [
            InlineKeyboardButton(
                text="💎Профессиональная гигиена полости рта всего за 3000 руб",
                callback_data="hygiene"
            )
        ],
        [
            InlineKeyboardButton(
                text="😁Брекет-система (производство США) от 1100 руб/мес",
                callback_data="brecket"
            )
        ],
        [InlineKeyboardButton(text="↩️На главное меню", callback_data="cancel")],
    ]
)
