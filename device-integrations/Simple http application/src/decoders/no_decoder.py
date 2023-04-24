from src.decoders.decoder import Decoder


class NoDecoder(Decoder):
    def __init__(self):
        super().__init__()
        self._name = "no-decoder"
