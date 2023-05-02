from src.decoders.dragino_nmds120 import DraginoNmdS120Decoder
from src.decoders.no_decoder import NoDecoder
from src.decoders.x_logic_nbiot_pulse_meter import XLogicNbiotPulseMeterDecoder


def get_decoder(name):
    if name == "x-logic-nbiot-pulse-meter":
        decoder = XLogicNbiotPulseMeterDecoder()
    elif name == "dragino-nmds120":
        decoder = DraginoNmdS120Decoder()
    else:
        decoder = NoDecoder()
    return decoder
