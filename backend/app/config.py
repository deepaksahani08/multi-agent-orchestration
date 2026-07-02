from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    GOOGLE_API_KEY:str
    MODEL_NAME:str = "gemini-3.1-flash-lite"
    TEMPERATURE:float=0.3

    model_config= SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )

@lru_cache
def get_seetings()->Settings:
    return Settings()

settings = get_seetings()