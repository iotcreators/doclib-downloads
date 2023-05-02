class Decoder:
    def __init__(self):
        self._name = ""

    def decode(self, data):
        """This function must return a dictionary"""
        return {}

    @staticmethod
    def _data_to_byte_array(data_hex_string):
        return bytes.fromhex(data_hex_string)
