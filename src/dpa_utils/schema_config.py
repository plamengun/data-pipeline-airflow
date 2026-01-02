from .base_config import BaseConfig
import yaml



class SchemaConfig(BaseConfig):
    def __init__(
            self,
            config_path: str,
            config_key: str,
            secret_key: str
            ):
        super().__init__(config_path=config_path, config_key=config_key, secret_key=secret_key)

    def construct_url(self) -> str:
        with open(self._config_path, "r") as f:
            config = yaml.safe_load(f)

        service_config = config[self._config_key]

        url_template = service_config["URL_TEMPLATE"]
        exchange = service_config["EXCHANGE"]

        url = url_template.format(
            exchange=exchange,
            api_token=self._get_api_token()
        )
        return url
    
    def _get_api_token(self):
        pass
