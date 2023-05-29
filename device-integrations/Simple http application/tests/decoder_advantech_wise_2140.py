import json

from src.arg_parser import get_arg_parser
from src.decoders.decoder_factory import get_decoder

ns = get_arg_parser()
decoder = get_decoder(ns.decoder)
decoded = decoder.decode(
    "810b3a500807000000136500005423e20700000800050004000000090005000400000006000500040003000000009f16746460091b00010"
    "0009f167464ad")
print(json.dumps(decoded, indent=4))
