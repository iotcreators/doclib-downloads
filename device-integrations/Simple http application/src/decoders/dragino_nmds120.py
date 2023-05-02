import datetime

from src.decoders.decoder import Decoder


class DraginoNmdS120Decoder(Decoder):
    def __init__(self,):
        super().__init__()
        self._name = "dragino-nmds120"

    def decode(self, data):
        try:
            sw_version_raw_hex = data[16:20]
            battery_lvl_raw_hex = data[20:24]
            signal_strength_raw_hex = data[24:26]
            mod_raw_hex = data[26:28]
            exit_flag_raw_hex = data[28:30]
            distance1_raw_hex = data[30:34]
            distance2_raw_hex = data[34:38]
            unix_timestamp_raw = int(data[38:46], 16)
            decoded = {
                "imei": data[1:16],
                "sw_version": int(sw_version_raw_hex, 16),
                "battery_voltage_volt": int(battery_lvl_raw_hex, 16)/1000,
                "signal_strength": int(signal_strength_raw_hex, 16),
                "mod": int(mod_raw_hex, 16),
                "exit_flag": int(exit_flag_raw_hex, 16),
                "distance1_meters": int(distance1_raw_hex, 16)/100,
                "distance2_meters": int(distance2_raw_hex, 16)/100,
                "unix_timestamp_raw": unix_timestamp_raw,
                "timestamp_readable": datetime.datetime.fromtimestamp(unix_timestamp_raw).strftime('%Y-%m-%d %H:%M:%S')
            }
        except Exception as ex:
            print(f"Exception {str(ex)} has occurred while trying to decode data")
            decoded = {}

        return decoded
