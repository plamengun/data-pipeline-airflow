from abc import ABC, abstractmethod
from dotenv import load_dotenv

load_dotenv()

class BaseConfig(ABC):
    def __init__(self, config_path: str, config_key: str, secret_key: str = None):
        if not config_path:
            raise ValueError("config_path is required")
        if not config_key:
            raise ValueError("config_key is required")
        self._config_path = config_path
        self._config_key = config_key
        self._secret_key= secret_key

    @abstractmethod
    def _load_config(self):
        raise NotImplementedError("Config class should override load_config method from parent.")