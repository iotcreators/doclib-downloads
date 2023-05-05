from src.decoders.dragino_n95s31b import DraginoN95s31bDecoder
from src.decoders.dragino_nds03a import DraginoNds03aDecoder
from src.decoders.dragino_nlms01 import DraginoNlms01Decoder
from src.decoders.dragino_nmds120 import DraginoNmdS120Decoder
from src.decoders.dragino_nse01 import DraginoNse01Decoder
from src.decoders.dragino_nsph01 import DraginoNsph01Decoder
from src.decoders.no_decoder import NoDecoder
from src.decoders.x_logic_nbiot_pulse_meter import XLogicNbiotPulseMeterDecoder


def get_decoder(name):
    if name == "x-logic-nbiot-pulse-meter":
        decoder = XLogicNbiotPulseMeterDecoder()
    elif name == "dragino-nmds120":
        decoder = DraginoNmdS120Decoder()
    elif name == "dragino-nse01":
        decoder = DraginoNse01Decoder()
    elif name == "dragino-nsph01":
        decoder = DraginoNsph01Decoder()
    elif name == "dragino-nlms01":
        decoder = DraginoNlms01Decoder()
    elif name == "dragino-n95s31b":
        decoder = DraginoN95s31bDecoder()
    elif name == "dragino-nds03a":
        decoder = DraginoNds03aDecoder()
    else:
        decoder = NoDecoder()
    return decoder
