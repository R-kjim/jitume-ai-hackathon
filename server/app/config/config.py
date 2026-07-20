from pydantic_settings import BaseSettings, SettingsConfigDict

env_file = ".env"

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

variables=Variable()