from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./arthaquant.db"
    REDIS_URL: str = "redis://localhost:6379"
    JWT_SECRET: str = "CHANGE_ME"
    ENV: str = "dev"

    class Config:
        env_file = ".env"


settings = Settings()
