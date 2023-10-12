"""
Клавиатура списка акций
"""
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo

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

"""
Клавиатуры акций
"""

osstem_keyboard = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Подробнее об акции",
                web_app=WebAppInfo(url="https://demokrat-nn.ru/stocks"),
            )
        ],
        [InlineKeyboardButton(text="🌐Записаться по акции", callback_data="rec_online")],
        [InlineKeyboardButton(text="↩️На главное меню", callback_data="cancel")],
    ],
)

brecket_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Подробнее об акции",
                web_app=WebAppInfo(url="https://demokrat-nn.ru/stocks"),
            )
        ],
        [InlineKeyboardButton(text="🌐Записаться по акции", callback_data="rec_online")],
        [InlineKeyboardButton(text="↩️На главное меню", callback_data="cancel")],
    ]
)

hygiene_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Подробнее об акции",
                web_app=WebAppInfo(url="https://demokrat-nn.ru/stocks"),
            )
        ],
        [InlineKeyboardButton(text="🌐Записаться по акции", callback_data="rec_online")],
        [InlineKeyboardButton(text="↩️На главное меню", callback_data="cancel")],
    ]
)
