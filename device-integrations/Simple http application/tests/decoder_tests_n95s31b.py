import json

from src.arg_parser import get_arg_parser
from src.decoders.decoder_factory import get_decoder

ns = get_arg_parser()
decoder = get_decoder(ns.decoder)
decoded = decoder.decode("f868411056758782000c0d0f0c0100000000300114023163199d3c0113023163199d120113023163199c5e01120"
                         "23763199baa0112023263199af60111023b631999a70112023b631998f3011202426319983f01110242631996eb",
                         version=ns.version)
print(json.dumps(decoded, indent=4))
