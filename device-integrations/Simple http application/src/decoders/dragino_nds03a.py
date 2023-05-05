import datetime
from src.decoders.dragino import DraginoDecoder


class DraginoNds03aDecoder(DraginoDecoder):
    def __init__(self, ):
        super().__init__()
        self._name = "dragino-nsph01"

    def decode(self, data, version=0):
        try:
            self._mod_len = 2
            decoded = super().decode(data)
            start = self._start_index
            decoded["door_status"]: int(data[start:start + 2], 16)
            decoded["alarm_status"]: int(data[start + 2:start + 4], 16)
            decoded["door_open_num"] = int(data[start + 4:start + 10], 16)
            decoded["last_open_time"] = int(data[start + 10:start + 16], 16)
            unix_timestamp_raw = int(data[start + 16:start + 24], 16)
            decoded["unix_timestamp_raw"] = unix_timestamp_raw
            decoded["timestamp_readable"] = \
                datetime.datetime.fromtimestamp(unix_timestamp_raw).strftime('%Y-%m-%d %H:%M:%S')
            index = start + 24
            data_array = []
            data_len = len(data)
            while index < data_len:
                temp_decoded = {
                    "door_status": int(data[index:index + 2], 16),
                    "door_open_num": int(data[index + 2:index + 8], 16),
                    "last_open_time": int(data[index + 8:start + 14], 16),
                    "unix_timestamp_raw": int(data[index + 14:index + 22], 16),
                    "timestamp_readable": datetime.datetime.fromtimestamp(int(data[index + 8:index + 16], 16)).
                        strftime('%Y-%m-%d %H:%M:%S')
                }
                data_array.append(temp_decoded)
                index += 22

            decoded["data_recorded"] = data_array
        except Exception as ex:
            print(f"Exception {str(ex)} has occurred while trying to decode data")
            decoded = {}

        return decoded
