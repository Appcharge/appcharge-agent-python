from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=(".env"), case_sensitive=True)
    APP_PORT: int
    OFFERS_FILE_PATH: str
    PLAYER_DATASET_FILE_PATH: str
    PUBLISHER_TOKEN: str
    FACEBOOK_APP_SECRET: str
    KEY: str
    REPORTING_API_URL: str
    ASSET_UPLOAD_GATEWAY_URL: str
    AWARD_PUBLISHER_URL: str


def get_settings() -> Settings:
    return Settings()
