import datetime
from src.decoders.dragino import DraginoDecoder


class DraginoNmdS120Decoder(DraginoDecoder):
    def __init__(self,):
        super().__init__()
        self._name = "dragino-nmds120"

    def decode(self, data, version=0):
        try:
            if int(version) < 132:
                decoded = {
                    "device_id": data[0:12],
                    "sw_version": int(data[12:16], 16),
                    "battery_voltage_volt": int(data[16:20], 16) / 1000,
                    "signal_strength": int(data[20:22], 16),
                    "distance": int(data[22:26], 16),
                    "interrupt": int(data[26:28], 16)
                }
            else:
                self._mod_len = 2
                decoded = super().decode(data)
                start = self._start_index
                decoded["interrupt"] = int(data[start:start+2], 16)
                index = start + 2
                data_array = []
                data_len = len(data)
                while index < data_len:
                    temp_decoded = {
                        "distance": int(data[index:index + 4], 16),
                        "unix_timestamp_raw": int(data[index + 4:index + 12], 16),
                        "timestamp_readable": datetime.datetime.fromtimestamp(int(data[index + 4:index + 12], 16)).
                            strftime('%Y-%m-%d %H:%M:%S')
                    }
                    data_array.append(temp_decoded)
                    index += 12

                decoded["data_recorded"] = data_array
        except Exception as ex:
            print(f"Exception {str(ex)} has occurred while trying to decode data")
            decoded = {}

        return decoded
