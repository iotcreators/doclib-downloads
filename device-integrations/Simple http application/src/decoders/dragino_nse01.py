import datetime
from src.decoders.dragino import DraginoDecoder


class DraginoNse01Decoder(DraginoDecoder):
    def __init__(self, ):
        super().__init__()
        self._name = "dragino-nse01"

    def decode(self, data, version=0):
        try:
            decoded = super().decode(data)
            soil_moisture_raw_hex = data[30:34]
            soil_temperature_raw_hex = data[34:38]
            soil_conductivity_raw_hex = data[38:42]
            soil_dielectric_raw_hex = data[42:46]
            interrupt_raw_hex = data[28:30]
            decoded["interrupt"]: int(interrupt_raw_hex, 16)
            unix_timestamp_raw = int(data[46:54], 16)
            decoded["soil_moisture"] = int(soil_moisture_raw_hex, 16) / 100
            decoded["soil_temperature_celsius"] = int(soil_temperature_raw_hex, 16) / 100
            decoded["soil_conductivity"] = int(soil_conductivity_raw_hex, 16)
            decoded["soil_dielectric_constant"] = int(soil_dielectric_raw_hex, 16)
            decoded["unix_timestamp_raw"] = unix_timestamp_raw
            decoded["timestamp_readable"] = \
                datetime.datetime.fromtimestamp(unix_timestamp_raw).strftime('%Y-%m-%d %H:%M:%S')
            if decoded["sw_version"] >= 132:
                index = 54
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
