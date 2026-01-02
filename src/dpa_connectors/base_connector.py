from abc import ABC, abstractmethod
from ..dpa_utils.base_config import BaseConfig

class BaseConnector(ABC):
    '''
    This is a base class for all Connectors. It establishes the base contract for child classes.
    '''
    def __init__(self, config: BaseConfig, synch_path: str):
        self.config = config
        self.synch_path = synch_path
        
    @abstractmethod
    def get_raw_data(self):
        raise NotImplementedError("Connector class should override get_raw_data method from parent.")

    @abstractmethod
    def write_raw_data(self):
        raise NotImplementedError("Connector class should override write_raw_data method from parent.")

    @abstractmethod
    def load_config(self):
        raise NotImplementedError("Connector class should override load_config method from parent.")