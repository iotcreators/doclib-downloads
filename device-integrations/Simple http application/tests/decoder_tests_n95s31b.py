import json

from src.arg_parser import get_arg_parser
from src.decoders.decoder_factory import get_decoder

ns = get_arg_parser()
decoder = get_decoder(ns.decoder)
decoded = decoder.decode("f86778705152152800830e1d1f01000000002800ef02306454d27800ef02176454cf650000000000000000000000"
                         "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
                         version=ns.version)
print(json.dumps(decoded, indent=4))
