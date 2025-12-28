from abc import ABC, abstractmethod
from dotenv import load_dotenv

load_dotenv()

class BaseConfig(ABC):
    def __init__(self, config_path: str, config_key: str, secret_key: str):
        if not config_path:
            raise ValueError("config_path is required")
        if not config_key:
            raise ValueError("config_key is required")
        if not secret_key:
            raise ValueError("secret_env_var is required")

        self._config_path = config_path
        self._config_key = config_key
        self._secret_key= secret_key

    @abstractmethod
    def construct_url(self) -> str:
        raise NotImplementedError("Config class should override construct_url method from parent.")
    
    @abstractmethod
    def _get_api_token(self) -> str:
        raise NotImplementedError("Config class should override get_api_token method from parent.")
