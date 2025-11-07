from pydantic_settings import BaseSettings, SettingsConfigDict


class SQLiteSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="SQLITE_", env_file=".env")

    FILE_NAME: str = "example"

    @property
    def sqlalchemy_sync_sqlite_url(self) -> str:
        return f"sqlite:///{self.FILE_NAME}.db"

    @property
    def sqlalchemy_async_sqlite_url(self) -> str:
        return f"sqlite+aiosqlite:///{self.FILE_NAME}.db"


sqlite_settings = SQLiteSettings()
