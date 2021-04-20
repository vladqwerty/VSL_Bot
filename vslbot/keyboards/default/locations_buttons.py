from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keybord = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Send location', request_location=True)
        ]
    ]
)