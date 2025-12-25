import requests
from .base_connector import BaseConnector
from ..dpa_utils.base_config import BaseConfig
from ..dpa_utils.api_config import APIConfig


class APIConnector(BaseConnector):
    def __init__(self, config: BaseConfig):
        super().__init__(config=config)

    def get_raw_data(self):
        """Get companies from EODHD API using Airflow variable"""
        try:
            url = self.config.construct_url()
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching EODHD data: {e}")
            raise

    def write_raw_data(self):
        pass

    def load_config(self):
        pass