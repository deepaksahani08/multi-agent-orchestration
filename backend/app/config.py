from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    GOOGLE_API_KEY:str
    MODEL_NAME:str = "gemini-3.1-flash-lite"
    TEMPERATURE:float=0.3

    LANGSMITH_API_KEY:str | None = None
    LANGSMITH_TRACING:bool = False
    LANGSMITH_PROJECT:str = "multi-agent-orchestration"

    model_config= SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

@lru_cache
def get_settings()->Settings:
    return Settings()

settings = get_settings()