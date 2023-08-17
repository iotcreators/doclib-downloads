import json

from src.arg_parser import get_arg_parser
from src.decoders.decoder_factory import get_decoder

ns = get_arg_parser()
decoder = get_decoder(ns.decoder)
decoded = decoder.decode("03581a222b033a", version=ns.version)
print(json.dumps(decoded, indent=4))
