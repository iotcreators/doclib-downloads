from src.decoders.decoder import Decoder


class DraginoDecoder(Decoder):
    def __init__(self,):
        super().__init__()
        self._name = "dragino"

    def _decode_dragino_commons(self, data):
        self._print_log(f"Decoding common fields")
        sw_version_raw_hex = data[16:20]
        battery_lvl_raw_hex = data[20:24]
        signal_strength_raw_hex = data[24:26]
        mod_raw_hex = data[26:28]
        decoded = {
            "imei": data[1:16],
            "sw_version": int(sw_version_raw_hex, 16),
            "battery_voltage_volt": int(battery_lvl_raw_hex, 16) / 1000,
            "signal_strength": int(signal_strength_raw_hex, 16),
            "mod": int(mod_raw_hex, 16)
        }

        return decoded

    def decode(self, data):
        return self._decode_dragino_commons(data)
