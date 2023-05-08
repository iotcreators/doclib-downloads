import json

from src.arg_parser import get_arg_parser
from src.decoders.decoder_factory import get_decoder

ns = get_arg_parser()
decoder = get_decoder(ns.decoder)
decoded = decoder.decode("f86778705021331700840cfd1b010000000ae80000000a6315537b0110034306f7004663185f19010f034306f7"
                         "004663185b950105034606eb00476315c7790102034a0000000a6315c3f5010303410000000a6315c071010403"
                         "46000000006315bced01040346000000006315b96901040341000000006315b5e5",
                         version=ns.version)
print(json.dumps(decoded, indent=4))
