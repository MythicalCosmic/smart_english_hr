"""
Message handlers
"""
from aiogram import Router, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.filters.custom import ButtonTextFilter
from bot.keyboards.reply import get_language_selection_keyboard, get_main_reply_keyboard, get_info_button
from bot.keyboards.variables import english, uzbek, russian
from bot.states.user import UserStates
from core.settings import get_translation, get_button_text
from utils.helpers import set_user_language, set_user_state, get_user_language, get_user_state, user_exists

router = Router()

admin_id = [6589960007]


@router.message(StateFilter(UserStates.language))
async def set_language(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language_text = message.text.lower()

        language_map = {
            english.lower(): 'en',
            uzbek.lower(): 'uz',
            russian.lower(): 'ru'
        }

        if language_text not in language_map:
            await message.answer(
                get_translation('welcome_new', 'uz'),
                reply_markup=get_language_selection_keyboard(),
                parse_mode="html"
            )
            return

        language_code = language_map[language_text]

        await set_user_language(user_id, language_code)

        await message.answer(
            get_translation('welcome_hh', language_code),
            reply_markup=get_main_reply_keyboard(language_code)
        )
        await state.set_state(UserStates.menu)
        await set_user_state(user_id, UserStates.menu.state)

    except Exception as e:
        await bot.send_message(chat_id=admin_id[0], text=str(e))

@router.message(ButtonTextFilter('job_vacancies'), StateFilter(UserStates.menu))
async def handle_job_vacancies(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = await get_user_language(user_id)
        await message.answer(get_translation('info', language), reply_markup=get_info_button(language), parse_mode="html")
        await state.set_state(UserStates.info)
        await set_user_state(user_id, UserStates.info.state)

    except Exception as e:
        await bot.send_message(chat_id=admin_id[0], text=str(e))

@router.message(StateFilter(UserStates.menu))
async def menu_handler(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = await get_user_language(user_id)
        await message.answer(get_translation('welcome_hh', language), reply_markup=get_main_reply_keyboard(language), parse_mode="html")
        await state.set_state(UserStates.menu)
        await set_user_state(user_id, UserStates.menu.state)

    except Exception as e:
        await message.reply(f"Error occurred: {e}")

@router.message()
async def fallback_handler(message: Message, state: FSMContext, bot: Bot):
    try:
        user_id = message.from_user.id
        language = await get_user_language(user_id)

        if user_exists(user_id) and language is not None:
            await message.answer(get_translation('welcome_back', language), reply_markup=get_main_reply_keyboard(language), parse_mode="html")
            await state.set_state(UserStates.menu)
            await set_user_state(user_id, UserStates.menu.state)

        else:
            await message.answer(get_translation('welcome_new', 'uz'), reply_markup=get_language_selection_keyboard(), parse_mode="html")
            await state.set_state(UserStates.language)
            await set_user_state(user_id, UserStates.language.state)

    except Exception as e:
        await bot.send_message(chat_id=admin_id[0], text=str(e))


