class Decoder:
    def __init__(self):
        self._name = ""

    def decode(self, data, version=0):
        """This function must return a dictionary"""
        return {}

    def _print_log(self, msg):
        print(f"[{self._name}] {msg}")

    @staticmethod
    def _data_to_byte_array(data_hex_string):
        return bytes.fromhex(data_hex_string)
