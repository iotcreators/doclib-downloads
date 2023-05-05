import datetime
from src.decoders.dragino import DraginoDecoder


class DraginoN95s31bDecoder(DraginoDecoder):
    def __init__(self, ):
        super().__init__()
        self._name = "dragino-n95s31b"

    def decode(self, data, version=0):
        try:
            if int(version) < 120:
                self._start_index = 0
                self._dev_id_len = 12
                self._mod_len = 2
                decoded = super().decode(data)
                start = self._start_index
                decoded["ignore"] = data[start:start + 10]
                decoded["temperature_sht31"] = int(data[start + 10:start + 14], 16) / 10
                decoded["humidity_sht31"] = int(data[start + 14:start + 18], 16) / 10
            else:
                self._mod_len = 2
                decoded = super().decode(data)
                start = self._start_index
                decoded["temperature_DS18B20"] = int(data[start:start+4], 16)
                decoded["interrupt"] = int(data[start+4:start + 6], 16)
                decoded["adc"] = int(data[start+6:start + 10], 16)
                index = start + 10
                data_array = []
                data_len = len(data)
                while index < data_len:
                    temp_decoded = {
                        "temperature_sht31": int(data[index:index + 4], 16) / 10,
                        "humidity_sht31": int(data[index + 4:index + 8], 16) / 10,
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
