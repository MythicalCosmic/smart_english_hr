"""
Command handlers
"""
from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot.keyboards.inline import get_main_keyboard
from bot.keyboards.reply import get_language_selection_keyboard, get_main_reply_keyboard
from bot.states.user import UserStates
from core.settings import ADMIN_ID, get_translation
from utils.helpers import get_user_language, user_exists, set_user_state

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = await get_user_language(user_id)

        if await user_exists(user_id) and language is not None:
            await message.answer(get_translation('welcome_back', language), reply_markup=get_main_reply_keyboard(language), parse_mode="html")
            await state.set_state(UserStates.menu)
            await set_user_state(user_id, UserStates.menu.state)

        else:
            await message.answer(get_translation('welcome_new', 'uz'), reply_markup=get_language_selection_keyboard(), parse_mode="html")
            await state.set_state(UserStates.language)
            await set_user_state(user_id, UserStates.language.state)

    except Exception as e:
        await bot.send_message(chat_id=ADMIN_ID, text=str(e))





@router.message(Command("help"))
async def cmd_help(message: Message):
    """Handle /help command"""
    await message.answer(
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message"
    )
