"""
Handler registration
"""
from aiogram import Dispatcher
from bot.handlers import commands, messages, callbacks

def register_handlers(dp: Dispatcher):
    """Register all handlers"""
    dp.include_router(commands.router)
    dp.include_router(messages.router)
    dp.include_router(callbacks.router)
