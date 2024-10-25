from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    PROJECT_NAME: str = "Infoeste 2024"
    ELASTIC_URL: str
    INDEX_ELASTIC: str
    
    ENV: str

    class Config:
        env_file = './.env'
settings = Settings()