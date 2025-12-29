"""
Helper functions
"""
from typing import Optional

from database.database import get_session
from database.models.user import User


def format_user_mention(user_id: int, name: str) -> str:
    """Format user mention for HTML"""
    return f'<a href="tg://user?id={user_id}">{name}</a>'


async def user_exists(user_id: int) -> bool:
    async for session in get_session():
        result = await session.get(User, user_id)
        return result is not None


async def add_user(
    user_id: int,
    first_name: Optional[str],
    last_name: Optional[str],
    username: Optional[str],
):
    async for session in get_session():
        existing_user = await session.get(User, user_id)
        if existing_user:
            return  # user already exists

        user = User(
            id=user_id,
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        session.add(user)
        await session.commit()


async def get_user(user_id: int) -> Optional[User]:
    async for session in get_session():
        return await session.get(User, user_id)


async def set_user_state(user_id: int, state: str) -> None:
    async for session in get_session():
        user = await session.get(User, user_id)
        if not user:
            return

        user.state = state
        await session.commit()


async def get_user_state(user_id: int) -> Optional[str]:
    async for session in get_session():
        user = await session.get(User, user_id)
        return user.state if user else None


async def get_user_language(user_id: int) -> Optional[str]:
    async for session in get_session():
        user = await session.get(User, user_id)
        return user.language if user else None


async def set_user_language(user_id: int, language: str) -> None:
    async for session in get_session():
        user = await session.get(User, user_id)
        if not user:
            return

        user.language = language
        await session.commit()