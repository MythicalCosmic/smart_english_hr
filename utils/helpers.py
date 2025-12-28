"""
Helper functions
"""
from database.database import  get_session
from database.models.user import User

def format_user_mention(user_id: int, name: str) -> str:
    """Format user mention for HTML"""
    return f'<a href="tg://user?id={user_id}">{name}</a>'


async def user_exists(user_id: int) -> bool:
    """Check if a user exists in the database"""
    async for session in get_session():
        result = await session.get(User, user_id)
        return result is not None
    return False


async def add_user(user_id: int, name: str, first_name: str, last_name: str, username: str):
    async with get_session() as session:
        user = User(
            id=user_id,
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        session.add(user)
        await session.commit()


async def get_user(user_id: int) -> User:
    async with get_session() as session:
        user = await session.get(User, user_id)
        return user

async def set_user_state(user_id: int, state: str):
    async with get_session() as session:
        user = await session.get(User, user_id)
        if user:
            user.state = state
            await session.commit()

async def get_user_state(user_id: int) -> User:
    async with get_session() as session:
        user = await session.get(User, user_id)
        if user:
            return user.state




