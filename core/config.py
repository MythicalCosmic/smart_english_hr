"""
Configuration management
"""
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv(override=True)

@dataclass
class Config:
    """Bot configuration"""
    bot_token: str
    database_url: str
    admin_ids: list[int]
    
    @classmethod
    def from_env(cls):
        """Load configuration from environment variables"""
        return cls(
            bot_token=os.getenv("BOT_TOKEN", ""),
            database_url=os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./bot_database.db"),
            admin_ids=[int(id) for id in os.getenv("ADMIN_IDS", "").split(",") if id]
        )

config = Config.from_env()
