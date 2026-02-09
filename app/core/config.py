from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    OPENAI_API_KEY: str = ""
    MONGO_URI: str = "mongodb://localhost:27017"
    DB_NAME: str = "cv_analyzer"
    DEFAULT_MODEL: str = "gpt-4o-mini"

    POPPLER_BIN: str = ""
    TESSERACT_CMD: str = ""

settings = Settings()
