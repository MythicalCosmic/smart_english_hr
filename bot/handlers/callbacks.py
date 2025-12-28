"""
Callback query handlers
"""
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()

@router.callback_query()
async def handle_callback(callback: CallbackQuery):
    """Handle callback queries"""
    await callback.answer("Button clicked!")
