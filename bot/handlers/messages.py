"""
Message handlers
"""
from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def echo_message(message: Message):
    """Echo all text messages"""
    await message.answer(f"You said: {message.text}")
