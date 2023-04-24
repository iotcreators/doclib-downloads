from src.decoders.decoder import Decoder


class XLogicNbiotPulseMeterDecoder(Decoder):
    def __init__(self,):
        super().__init__()
        self._name = "x-logic-nbiot-pulse-meter"

    def decode(self, data):
        try:
            byte_array = bytes.fromhex(data)
            data_decoded = byte_array.decode('utf-8')
            imei_start = data_decoded.find("IMEI: ")
            imei = data_decoded[imei_start + 6:imei_start + 21]
            params = {"imei": imei}
            msg = ""
            tamper = 0
            voltage = 0
            impulse1 = 0
            impulse2 = 0
            send_mode_parsed = ""
            temperature = 0
            mode = 0

            if (len(byte_array)) > 58:
                impulse1 = byte_array[3] << 24 | byte_array[2] << 16 | byte_array[1] << 8 | byte_array[0]
                impulse2 = byte_array[7] << 24 | byte_array[6] << 16 | byte_array[5] << 8 | byte_array[4] << 0

                data_as_int = [b for b in byte_array]
                voltage = byte_array[8] + 200
                mode = int(data_as_int[9])
                tamper = int(data_as_int[10])
                temperature = int(data_as_int[11])
                if mode == 0:
                    send_mode_parsed = "1h"
                if mode == 1:
                    send_mode_parsed = "2h"
                if mode == 2:
                    send_mode_parsed = "4h"
                if mode == 3:
                    send_mode_parsed = "8h"
                if mode == 4:
                    send_mode_parsed = "12h"
                if mode == 5:
                    send_mode_parsed = "24h"
                if mode == 6:
                    send_mode_parsed = "48h"
                msg = ""
                if tamper & 0b10000000:
                    msg = msg + "Tamper message\n"
            else:
                msg = msg + "Regular message\n"
            if tamper & 0b00000100:
                msg = msg + " Acc tamper active\n"
            if tamper & 0b00000010:
                msg = msg + " IN3 tamper active\n"
            if tamper & 0b00000001:
                msg = msg + " IN1 tamper active\n"

            decoded = {
                "voltage": voltage,
                "temperature": temperature,
                "tamper": tamper,
                "impulse1": impulse1,
                "impulse2": impulse2,
                "send_mode_parsed": send_mode_parsed,
                "mode": mode,
                "msg": msg,
                "params": params
            }
        except Exception as ex:
            print(f"unable to parse data, detected exception {str(ex)}")
            decoded = {}

        return decoded
