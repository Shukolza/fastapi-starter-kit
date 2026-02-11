from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    JWT_SECRET_KEY: str
    JWT_EXPIRE_MIN: int | None = None
    ALGORITHM: str = "HS256"
    DB_URL: str

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def ACCESS_TOKEN_EXPIRE_MIN(self) -> int | None:
        if self.JWT_EXPIRE_MIN == 0:
            return None
        return self.JWT_EXPIRE_MIN


settings = Settings()  # type: ignore
