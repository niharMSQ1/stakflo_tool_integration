from urllib.parse import quote_plus

from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "Tool Integrations API"
    api_v1_prefix: str = "/api/v1"

    db_name: str = Field(default="postgres", validation_alias="DB_NAME")
    tools_integrations_db_name: str = Field(
        default="postgres",
        validation_alias="TOOLS_INTEGRATIONS_DB_NAME",
    )
    db_user: str = Field(default="postgres", validation_alias="DB_USER")
    db_password: str = Field(default="", validation_alias="DB_PASSWORD")
    db_host: str = Field(default="localhost", validation_alias="DB_HOST")
    db_port: int = Field(default=5432, validation_alias="DB_PORT")

    @staticmethod
    def _dsn(database: str, user: str, password: str, host: str, port: int) -> str:
        u = quote_plus(user)
        p = quote_plus(password)
        return f"postgresql://{u}:{p}@{host}:{port}/{database}"

    @computed_field
    @property
    def database_url(self) -> str:
        return self._dsn(
            self.db_name,
            self.db_user,
            self.db_password,
            self.db_host,
            self.db_port,
        )

    @computed_field
    @property
    def tools_integrations_database_url(self) -> str:
        return self._dsn(
            self.tools_integrations_db_name,
            self.db_user,
            self.db_password,
            self.db_host,
            self.db_port,
        )


settings = Settings()
