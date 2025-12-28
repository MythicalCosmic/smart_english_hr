"""
Throttling middleware
"""
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message

class ThrottlingMiddleware(BaseMiddleware):
    """Middleware for rate limiting"""
    
    def __init__(self, rate_limit: int = 1):
        self.rate_limit = rate_limit
        super().__init__()
    
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        # Add rate limiting logic here
        return await handler(event, data)
