# Python
import os

# Pydantic
from pydantic import BaseSettings, validator

env_path = os.path.join(os.getcwd(), ".env")


class Settings(BaseSettings):
    class Config:
        case_sensitive = False
        env_file = env_path
        env_file_encoding = "utf-8"

    MONGO_URI: str
    PROJECT_NAME: str

    @validator("MONGO_URI", pre=True)
    def validate_mongo_uri(cls, v: str) -> str:
        if not v.startswith("mongodb+srv://"):
            raise ValueError("MONGO_URI must start with 'mongodb+srv://'")
        return v


settings = Settings()
