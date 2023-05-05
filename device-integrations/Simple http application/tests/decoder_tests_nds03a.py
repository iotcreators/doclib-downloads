import json

from src.arg_parser import get_arg_parser
from src.decoders.decoder_factory import get_decoder

ns = get_arg_parser()
decoder = get_decoder(ns.decoder)
decoded = decoder.decode("f867787051520942006f0dfb1901010000000000000064550826", version=ns.version)
print(json.dumps(decoded, indent=4))
