import requests
import pyarrow as pa
import pyarrow.parquet as pq
from .base_connector import BaseConnector
from ..dpa_utils.api_config import APIConfig

TYPE_REGISTRY = {
    "string": lambda spec: pa.string(),
    "int64":  lambda spec: pa.int64(),
    "float64": lambda spec: pa.float64(),
    "bool":   lambda spec: pa.bool_(),
    "date32": lambda spec: pa.date32(),
    "timestamp": lambda spec: pa.timestamp(
        spec.get("unit", "us"),
        tz=spec.get("timezone")
    ),
}

class APIConnector(BaseConnector):
    def __init__(self, config: APIConfig, synch_path: str):
        super().__init__(config=config, synch_path=synch_path)

    def get_raw_data(self):
        """Get companies data from API using Airflow variable"""
        try:
            url = self.config.construct_url()
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching raw data: {e}")
            raise

    def write_raw_data(self):
        """Write raw data to bronze"""
        data = self.get_raw_data()
        table = pa.Table.from_pylist(data)
        try:
            writer = pq.ParquetWriter(
                "/home/kimbuzi/Documents/Projects/data_bronze",
                table.schema,
                compression="snappy"
            )
            writer.write_table(table)
            print(f"Raw data successfully saved to bronze as parquet table!")
        except Exception as e:
            print(f"Error writing raw data to bronze from API: {e}")


    def build_arrow_schema(self, schema_spec: dict) -> pa.Schema:
        cols = schema_spec["columns"]
        pa_fields = []
        for c in cols:
            t = c["type"]
            if t not in TYPE_REGISTRY:
                raise ValueError(f"Unknown type '{t}' for column '{c['name']}'")
            pa_type = TYPE_REGISTRY[t](c)
            pa_fields.append(
                pa.field(c["name"], pa_type, nullable=c.get("nullable", True))
            )
        return pa.schema(pa_fields)


    def load_config(self):
        pass