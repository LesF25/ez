from functools import cached_property

from pydantic import Field, computed_field, PostgresDsn
from pydantic_settings import BaseSettings


class PostgresSettings(BaseSettings):
    user: str = Field(
        default='postgres',
        alias='POSTGRES_USER',
    )
    password: str = Field(
        default='postgres',
        alias='POSTGRES_PASSWORD',
    )
    host: str = Field(
        default='localhost',
        alias='POSTGRES_HOST',
    )
    port: int = Field(
        default=5432,
        alias='POSTGRES_PORT',
    )
    db_name: str = Field(
        default='ez_family_db',
        alias='POSTGRES_DB',
    )

    @computed_field
    @cached_property
    def url(self) -> str:
        return str(
            PostgresDsn.build(
                scheme='postgresql+asyncpg',
                username=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                path=self.db_name,
            )
        )


class CorsSettings(BaseSettings):
    origins: list[str] = [
        'http://localhost:9000',
        'http://127.0.0.1:9000',
    ]


class Settings(BaseSettings):
    debug: bool = Field(default=False, alias='DEBUG')
    cors: CorsSettings = CorsSettings()
    postgres: PostgresSettings = PostgresSettings()


settings = Settings()
