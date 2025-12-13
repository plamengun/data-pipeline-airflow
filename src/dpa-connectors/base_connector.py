
class BaseConnector():
    '''
    This is a base class for all Connectors. It extablishes the base contract for child classes.
    '''
    def __init__(self):
        pass

    def get_raw_data(self):
        pass

    def load_config(self):
        pass

    def write_raw_data(self):
        pass