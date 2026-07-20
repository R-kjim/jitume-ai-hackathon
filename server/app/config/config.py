from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env_file = BASE_DIR / ".env"


class Variable( BaseSettings):
    model_config = SettingsConfigDict (env_file= env_file, extra= "ignore")
    
    database_url: str
    async_database_url: str

    # access
    frontend_url: str
    backend_url: str
    auth_cookie_domain: str

    # jwt
    jwt_secret_key: str

    # openai
    openai_api: str

    postgres_host: str
    postgres_port: int
    postgres_name: str
    postgres_user: str
    postgres_password: str

    fathom_api_key:str
    fathom_webhook_secret: str

variables=Variable()