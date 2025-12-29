from sqlalchemy import Column, String, Date, Boolean, Integer, Enum
from database.models.base import Base
import enum


class GenderEnum(enum.Enum):
    male = "male"
    female = "female"


class LevelEnum(enum.Enum):
    beginner = "beginner"
    intermediate = "intermediate"
    advanced = "advanced"


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    birth_date = Column(Date, nullable=False)

    address = Column(String(255), nullable=False)
    phone_number = Column(String(20), nullable=False)

    is_student = Column(Boolean, default=False)

    knowledge_level = Column(
        Enum(LevelEnum),
        nullable=False
    )

    gender = Column(
        Enum(GenderEnum),
        nullable=False
    )

    russian_level = Column(Enum(LevelEnum), nullable=True)
    russian_level_voice_path = Column(String(255), nullable=True)

    english_level = Column(Enum(LevelEnum), nullable=True)
    english_level_voice_path = Column(String(255), nullable=True)

    ielts_certificate_path = Column(String(255), nullable=True)

    work_experience = Column(String(255), nullable=True)
    last_workplace = Column(String(255), nullable=True)

    photo_path = Column(String(255), nullable=True)
    resume_path = Column(String(255), nullable=True)

    how_find_out = Column(String(255), nullable=True)
