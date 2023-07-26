from cayennelpp import LppFrame

from src.decoders.decoder import Decoder


class CayenneLLP(Decoder):
    def __init__(self, ):
        super().__init__()
        self._name = "cayenne-llp"

    def decode(self, data, version=0):
        byte_data = bytes.fromhex(data)
        buffer = bytearray(byte_data)
        frame = LppFrame().from_bytes(buffer)
        parsed = {}
        for lpp_data in frame:

            parsed[f"channel_{str(lpp_data.channel)}"] = {
                "type": str(lpp_data.type),
                "values": self.read_values(lpp_data)
            }
        return parsed

    def read_values(self, lpp_data):
        values = []
        for value in lpp_data.value:
            values.append(value)
        if len(values) == 1:
            return values[0]
        return values
