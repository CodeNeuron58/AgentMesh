"""Application configuration using Pydantic Settings."""
from functools import lru_cache
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Application settings."""
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )
    
    # App
    APP_NAME: str = "AgentMesh"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False
    
    # LLM
    OPENAI_API_KEY: Optional[str] = None
    DEFAULT_MODEL: str = "gpt-4-turbo"
    DEFAULT_TEMPERATURE: float = 0.1
    
    # LLMOps (LangSmith)
    LANGSMITH_API_KEY: Optional[str] = None
    LANGSMITH_PROJECT: str = "agentmesh"
    LANGSMITH_TRACING_V2: bool = True
    
    # Persistence
    DATABASE_URL: str = "sqlite+aiosqlite:///./agentmesh.db"
    CHECKPOINT_DB: str = "./checkpoints.db"
    
    # API Configurations
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000

@lru_cache
def get_settings() -> Settings:
    return Settings()