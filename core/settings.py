from dotenv import load_dotenv
import os
import yaml
import logging

logging.basicConfig(level=logging.INFO)

load_dotenv(override=True)



ADMIN_ID = int(os.getenv("ADMIN_IDS", "0").split(",")[0]) 

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LANGUAGES_FILE = os.path.join(BASE_DIR, "languages", "translations.yaml") 

with open(LANGUAGES_FILE, "r", encoding="utf-8") as file:    
    LANGUAGES = yaml.safe_load(file)

logging.info("Configuration loaded successfully")

def get_translation(key: str, language: str) -> str:
    keys = key.split(".")
    data = LANGUAGES.get(language, LANGUAGES['uz'])

    try:
        for k in keys:
            data = data[k]
        if isinstance(data, str):
            return data
    except (KeyError, TypeError):
        pass

    return f"[{language}:{key}]"

def get_button_text(button_key: str, language: str) -> str:
    return get_translation(f"buttons.{button_key}", language)