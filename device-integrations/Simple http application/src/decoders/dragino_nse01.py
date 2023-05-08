import datetime
from src.decoders.dragino import DraginoDecoder


class DraginoNse01Decoder(DraginoDecoder):
    def __init__(self, ):
        super().__init__()
        self._name = "dragino-nse01"

    def decode(self, data, version=0):
        try:
            self._mod_len = 2
            decoded = super().decode(data)
            start = self._start_index
            decoded["interrupt"] = int(data[start:start+2], 16)
            start += 2
            soil_moisture_raw_hex = data[start:start+4]
            soil_temperature_raw_hex = data[start+4:start+8]
            soil_conductivity_raw_hex = data[start+8:start+12]
            soil_dielectric_raw_hex = data[start+12:start+16]
            unix_timestamp_raw = int(data[start+16:start+24], 16)
            decoded["soil_moisture"] = int(soil_moisture_raw_hex, 16) / 100
            decoded["soil_temperature_celsius"] = int(soil_temperature_raw_hex, 16) / 100
            decoded["soil_conductivity"] = int(soil_conductivity_raw_hex, 16)
            decoded["soil_dielectric_constant"] = int(soil_dielectric_raw_hex, 16)
            decoded["unix_timestamp_raw"] = unix_timestamp_raw
            decoded["timestamp_readable"] = \
                datetime.datetime.fromtimestamp(unix_timestamp_raw).strftime('%Y-%m-%d %H:%M:%S')
            if decoded["sw_version"] >= 132:
                index = start + 24
                data_array = []
                data_len = len(data)
                while index < data_len:
                    temp_decoded = {
                        "soil_temperature_celsius": int(data[index:index + 4], 16) / 100,
                        "soil_moisture": int(data[index + 4:index + 8], 16) / 100,
                        "soil_conductivity": int(data[index + 8:index + 12], 16) / 100,
                        "soil_dielectric_constant": int(data[index + 12:index + 16], 16) / 100,
                        "unix_timestamp_raw": int(data[index + 16:index + 24], 16),
                        "timestamp_readable": datetime.datetime.fromtimestamp(int(data[index + 16:index + 24], 16)).
                            strftime('%Y-%m-%d %H:%M:%S')
                    }
                    data_array.append(temp_decoded)
                    index += 24

                decoded["data_recorded"] = data_array
        except Exception as ex:
            print(f"Exception {str(ex)} has occurred while trying to decode data")
            decoded = {}

        return decoded
