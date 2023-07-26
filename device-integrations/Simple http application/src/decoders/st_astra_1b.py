from src.decoders.cayenne_llp import CayenneLLP
from src.decoders.decoder import Decoder


class STAstra1B(Decoder):
    def __init__(self, ):
        super().__init__()
        self._name = "st-astra-1b"

    def decode(self, data, version=0):
        cayenne_decoder = CayenneLLP()
        return cayenne_decoder.decode(data)
