"""
Command handlers
"""
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from bot.keyboards.inline import get_main_keyboard

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    """Handle /start command"""
    await message.answer(
        f"Hello, {message.from_user.first_name}!\n\n"
        "Welcome to your bot powered by Boundless-Aiogram.",
        reply_markup=get_main_keyboard()
    )





@router.message(Command("help"))
async def cmd_help(message: Message):
    """Handle /help command"""
    await message.answer(
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message"
    )
