"""
Custom filters
"""
from aiogram.filters import Filter
from aiogram.types import Message

class IsAdminFilter(Filter):
    """Filter for admin users"""
    
    async def __call__(self, message: Message) -> bool:
        from core.config import config
        return message.from_user.id in config.admin_ids
