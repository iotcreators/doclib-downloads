import datetime
from src.decoders.dragino import DraginoDecoder


class DraginoNlms01Decoder(DraginoDecoder):
    def __init__(self, ):
        super().__init__()
        self._name = "dragino-nsph01"

    def decode(self, data, version=0):
        try:
            decoded = super().decode(data)
            interrupt_raw_hex = data[28:30]
            decoded["interrupt"]: int(interrupt_raw_hex, 16)
            decoded["leaf_moisture"] = int(data[30:34], 16) / 10
            decoded["leaf_temperature_celsius"] = int(data[34:38], 16) / 10
            unix_timestamp_raw = int(data[38:46], 16)
            decoded["unix_timestamp_raw"] = unix_timestamp_raw
            decoded["timestamp_readable"] = \
                datetime.datetime.fromtimestamp(unix_timestamp_raw).strftime('%Y-%m-%d %H:%M:%S')
            index = 46
            data_array = []
            data_len = len(data)
            while index < data_len:
                temp_decoded = {
                    "leaf_temperature_celsius": int(data[index:index + 4], 16) / 10,
                    "leaf_moisture": int(data[index + 4:index + 8], 16) / 10,
                    "unix_timestamp_raw": int(data[index + 8:index + 16], 16),
                    "timestamp_readable": datetime.datetime.fromtimestamp(int(data[index + 8:index + 16], 16)).
                        strftime('%Y-%m-%d %H:%M:%S')
                }
                data_array.append(temp_decoded)
                index += 16

            decoded["data_recorded"] = data_array
        except Exception as ex:
            print(f"Exception {str(ex)} has occurred while trying to decode data")
            decoded = {}

        return decoded
