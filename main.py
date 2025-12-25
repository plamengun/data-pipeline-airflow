from src.dpa_connectors.api_connector import APIConnector
from src.dpa_utils.api_config import APIConfig


config = APIConfig('src/configs/connector_config.yml', 'EODHD', 'EODHD_TOKEN')
inst = APIConnector(config)

print(inst.get_raw_data())

