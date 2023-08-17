from src.decoders.decoder import Decoder


class NanosensoricsCarbonless(Decoder):
    def __init__(self, ):
        super().__init__()
        self._name = "nanosensorics-carbonless"

    def decode(self, data, version=0):
        co2_msb = int(data[0:2], 16)
        co2_lsb = int(data[2:4], 16)
        temp_dec = int(data[4:6], 16)
        temp_aftercomma = int(data[6:8], 16)
        batt_dec = int(data[10:12], 16)
        batt_aftercomma = int(data[12:14], 16)

        return {
            "co2": (co2_msb << 8) | co2_lsb,
            "temp": temp_dec + (temp_aftercomma/100),
            "humidity": int(data[8:10], 16),
            "battery": batt_dec + (batt_aftercomma/100)
        }
