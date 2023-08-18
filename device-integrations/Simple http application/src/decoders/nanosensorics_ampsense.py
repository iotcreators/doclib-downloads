from src.decoders.decoder import Decoder


class NanosensoricsAmpsense32(Decoder):
    def __init__(self, ):
        super().__init__()
        self._name = "nanosensorics-ampsense32"

    def decode(self, data, version=0):
        batt_dec = int(data[12:14], 16)
        batt_aftercomma = int(data[14:16], 16)

        return {
            "currentA": ((int(data[0:2], 16) << 8) | int(data[2:4], 16))/100,
            "currentB": ((int(data[4:6], 16) << 8) | int(data[6:8], 16))/100,
            "currentC": ((int(data[8:10], 16) << 8) | int(data[10:12], 16))/100,
            "battery": batt_dec + (batt_aftercomma/100)
        }
