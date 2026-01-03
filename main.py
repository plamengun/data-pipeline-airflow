from src.dpa_connectors.api_connector import APIConnector
from src.dpa_utils.api_config import APIConfig
from src.dpa_utils.schema_config import SchemaConfig


# config = APIConfig('src/configs/connector_config.yml', 'EODHD', 'EODHD_TOKEN')
# inst = APIConnector(config, "/home/kimbuzi/Documents/Projects/bronze_dump.txt")

# print(inst.write_raw_data())

config = SchemaConfig('src/configs/schemas_config.yml', 'schemas.eodhd_tickers_v1')
schema = config.data
print(schema["partition_cols"])