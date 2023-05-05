from src.decoders.decoder import Decoder


class DraginoDecoder(Decoder):
    def __init__(self,):
        super().__init__()
        self._name = "dragino"
        self._start_index = 1
        self._dev_id_len = 15
        self._sw_version_len = 4
        self._bat_lvl_len = 4
        self._signal_strength_len = 2
        self._mod_len = 4

    def _decode_dragino_commons(self, data):
        self._print_log(f"Decoding common fields")
        start = self._start_index
        end = self._start_index+self._dev_id_len
        imei = data[start:end]
        start = end
        end = start + self._sw_version_len
        sw_version_raw_hex = data[start:end]
        start = end
        end = start + self._bat_lvl_len
        battery_lvl_raw_hex = data[start:end]
        start = end
        end = start + self._signal_strength_len
        signal_strength_raw_hex = data[start:end]
        start = end
        end = start + self._mod_len
        mod_raw_hex = data[start:end]
        decoded = {
            "imei": imei,
            "sw_version": int(sw_version_raw_hex, 16),
            "battery_voltage_volt": int(battery_lvl_raw_hex, 16) / 1000,
            "signal_strength": int(signal_strength_raw_hex, 16),
            "mod": int(mod_raw_hex, 16)
        }
        self._start_index = end

        return decoded

    def decode(self, data, version=0):
        return self._decode_dragino_commons(data)
