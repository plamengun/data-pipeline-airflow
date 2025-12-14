from abc import ABC, abstractmethod

class BaseConnector(ABC):
    '''
    This is a base class for all Connectors. It extablishes the base contract for child classes.
    '''
    def __init__(self):
        pass

    @abstractmethod
    def get_raw_data(self):
        raise NotImplementedError("Connector class should override get_raw_data method from parent.")

    @abstractmethod
    def write_raw_data(self):
        raise NotImplementedError("Connector class should override write_raw_data method from parent.")

    def load_config(self):
        pass