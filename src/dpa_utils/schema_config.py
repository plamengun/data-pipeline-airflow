from .base_config import BaseConfig
import yaml


class SchemaConfig(BaseConfig):
    def __init__(
            self,
            config_path: str,
            config_key: str
            ):
        super().__init__(config_path=config_path, config_key=config_key)
        self.data = self._load_config()

    def _load_config(self):
        with open(self._config_path, "r") as f:
            config = yaml.safe_load(f)
        value =  config
        for key in self._config_key.split("."):
            value = value[key]
        return value
 
