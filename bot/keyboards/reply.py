"""
Reply keyboards
"""



from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from core.settings import get_translation
from .variables import english, uzbek, russian

def get_main_reply_keyboard(language: str = 'uz') -> ReplyKeyboardMarkup:
    """Get main reply keyboard"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=get_translation('buttons.job_vacancies', language))],
            [
                KeyboardButton(text=get_translation('buttons.about', language)),
                KeyboardButton(text=get_translation('buttons.feedback', language))
            ],
            [
                KeyboardButton(text=get_translation('buttons.contact', language)),
                KeyboardButton(text=get_translation('buttons.settings', language))
            ]
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

def get_info_button(language: str = 'uz') -> ReplyKeyboardMarkup:
    """Get info button"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=get_translation('buttons.survey', language))],
            [KeyboardButton(text=get_translation('buttons.back', language))],
        ],
        resize_keyboard=True
    )
    return keyboard

def get_back_button(language: str = 'uz') -> ReplyKeyboardMarkup:
    """Get back button"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=get_translation('buttons.back', language))],
        ],
        resize_keyboard=True
    )
    return keyboard
