from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///./local.db"
    source_url: str = ""

settings = Settings()