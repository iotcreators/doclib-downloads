import json

from src.decoders.decoder import Decoder
from src.decoders.utils.decoder_advantech_wise_2140 import decoder_advantech_wise_2140


class AdvantechWise2140(Decoder):
    def __init__(self, ):
        super().__init__()
        self._name = "advantech-wise-2140"

    def decode(self, data, version=0):
        json_string = decoder_advantech_wise_2140.decode(data)
        return json.loads(json_string)
