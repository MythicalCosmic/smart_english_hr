"""
Inline keyboards
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_main_keyboard() -> InlineKeyboardMarkup:
    """Get main inline keyboard"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Button 1", callback_data="btn_1")],
        [InlineKeyboardButton(text="Button 2", callback_data="btn_2")]
    ])
    return keyboard
