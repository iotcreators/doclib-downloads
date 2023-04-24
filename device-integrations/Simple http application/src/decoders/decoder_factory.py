from src.decoders.no_decoder import NoDecoder
from src.decoders.x_logic_nbiot_pulse_meter import XLogicNbiotPulseMeterDecoder


def get_decoder(name):
    if name == "x-logic-nbiot-pulse-meter":
        decoder = XLogicNbiotPulseMeterDecoder()
    else:
        decoder = NoDecoder()
    return decoder
