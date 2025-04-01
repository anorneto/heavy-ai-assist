
from pydantic_settings import BaseSettings


class EnvConfig(BaseSettings):
    """
    Environment configuration settings.
    """
    # Define environment variables with default values
    HEVY_API_KEY: str
    HEVY_API_URL: str
    DEBUG: bool = True
    LOG_LEVEL: str = "DEBUG"
    
    class Config:
        env_file = ".env"  # Specify the path to the .env file
        env_file_encoding = 'utf-8'  # Specify the encoding of the .env file