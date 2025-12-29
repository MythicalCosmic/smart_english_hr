"""
Custom filters
"""
from aiogram.filters import Filter
from aiogram.types import Message

from core.settings import get_button_text
from utils.helpers import get_user_language


class IsAdminFilter(Filter):
    """Filter for admin users"""
    
    async def __call__(self, message: Message) -> bool:
        from core.config import config
        return message.from_user.id in config.admin_ids


class ButtonTextFilter(Filter):
    def __init__(self, button_key: str):
        self.button_key = button_key

    async def __call__(self, message: Message) -> bool:
        if not message.text:
            return False
        language = await get_user_language(message.from_user.id)
        return message.text == get_button_text(self.button_key, language)