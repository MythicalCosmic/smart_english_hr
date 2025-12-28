"""
Main bot entry point
"""
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from core.config import config
from core.logging import setup_logging
from database.database import init_db, engine
from bot.handlers import register_handlers
from bot.middlewares.auth import AuthMiddleware
from bot.middlewares.throttling import ThrottlingMiddleware

load_dotenv()
setup_logging()

logger = logging.getLogger(__name__)

async def main():
    bot = Bot(
        token=config.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    dp.message.middleware(ThrottlingMiddleware())
    dp.message.middleware(AuthMiddleware())

    try:
        await init_db()
        logger.info("Database initialized")

        register_handlers(dp)
        logger.info("Handlers registered")

        logger.info("Bot started")
        await dp.start_polling(
            bot,
            allowed_updates=dp.resolve_used_update_types(),
            drop_pending_updates=True
        )

    except Exception as e:
        logger.error(f"Error during polling: {e}")

    finally:
        logger.info("Shutting down...")
        
        try:
            await bot.session.close()
        except Exception as e:
            logger.error(f"Error closing bot session: {e}")
        
        try:
            await engine.dispose()
        except Exception as e:
            logger.error(f"Error disposing engine: {e}")

        logger.info("Resources cleaned up")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped")