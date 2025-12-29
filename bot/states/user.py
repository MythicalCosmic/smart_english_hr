"""
FSM states
"""
from aiogram.fsm.state import State, StatesGroup

class UserStates(StatesGroup):
    """User FSM states"""
    start = State()
    language = State()
    menu = State()
    job_vacancies = State()
    info = State()
    first_name = State()
    last_name = State()
    birth_date = State()
    address = State()
    phone_number = State()
    is_student = State() #first half
    knowledge_level = State()
    gender = State()
    russian_level = State()
    russian_voice = State()
    english_level = State()
    english_voice = State()
    ielts_certificate = State() #last
    work_experience = State()
    last_workplace = State()
    photo = State()
    resume = State()
    how_find_out = State()
    confirmation = State()
