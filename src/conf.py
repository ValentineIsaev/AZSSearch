from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class ApiSettings(BaseSettings):
    model_config = ConfigDict(env_file='../.env')
