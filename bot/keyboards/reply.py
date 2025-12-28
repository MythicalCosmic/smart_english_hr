"""
Reply keyboards
"""



from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from variables import english, uzbek, russian

def get_main_reply_keyboard() -> ReplyKeyboardMarkup:
    """Get main reply keyboard"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Option 1")],
            [KeyboardButton(text="Option 2")]
        ],
        resize_keyboard=True
    )
    return keyboard


def get_language_selection_keyboard() -> ReplyKeyboardMarkup:
    """Get language selection reply keyboard"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=english)],
            [KeyboardButton(text=uzbek)],
            [KeyboardButton(text=russian)]
        ],
        resize_keyboard=True
    )
    return keyboard