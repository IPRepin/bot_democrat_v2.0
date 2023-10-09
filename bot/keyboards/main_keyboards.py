from aiogram.utils.keyboard import ReplyKeyboardBuilder, \
    KeyboardButton

main_menu = ReplyKeyboardBuilder()

main_menu.row(
    KeyboardButton(
        text="💫Акции и скидки"
    ),
)
main_menu.row(
    KeyboardButton(text="📑Ваши записи"),
    KeyboardButton(text="✅Записаться на прием"),
)
main_menu.row(
    KeyboardButton(text="🚕Такси до клиники"),
)

main_menu.row(
    KeyboardButton(text="🤩Скидка 5️% за отзыв о клинике"),
)
