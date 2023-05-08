import json

from src.arg_parser import get_arg_parser
from src.decoders.decoder_factory import get_decoder

ns = get_arg_parser()
decoder = get_decoder(ns.decoder)
decoded = decoder.decode("f867787051521544006f0e091b010001000000000000006458f313000000000000000000000000000000000000"
                         "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
                         "00000000000000000000000000000000000000000000000000",
                         version=ns.version)
print(json.dumps(decoded, indent=4))
