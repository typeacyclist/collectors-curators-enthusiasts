from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = "development"
    database_url: str = "sqlite:///./cce.db"
    session_secret: str = "dev-only-change-me"
    auth_mode: str = "dev"
    dev_admin_email: str = "admin@parkcityorchids.example"
    dev_admin_name: str = "PCO Administrator"
    public_base_url: str = "http://localhost:8080"
    firebase_api_key: str = ""
    firebase_auth_domain: str = ""
    firebase_project_id: str = ""
    default_tenant_name: str = "Park City Orchids and More"
    default_tenant_short_name: str = "PCO"
    default_timezone: str = "America/Denver"
    default_currency: str = "USD"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
