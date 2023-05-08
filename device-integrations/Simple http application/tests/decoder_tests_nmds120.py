import json

from src.arg_parser import get_arg_parser
from src.decoders.decoder_factory import get_decoder

ns = get_arg_parser()
decoder = get_decoder(ns.decoder)
decoded = decoder.decode("f86778705021331700840cf41e010000396315537b00396319baf000396319ba3c00396319b98800396319b8d40"
                         "0396319b82000396319b76c00396319b6b800396319b604",
                         version=ns.version)
print(json.dumps(decoded, indent=4))
