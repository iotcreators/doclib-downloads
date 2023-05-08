import json

from src.arg_parser import get_arg_parser
from src.decoders.decoder_factory import get_decoder

ns = get_arg_parser()
decoder = get_decoder(ns.decoder)
decoded = decoder.decode("f86841105675413800640c781701000225010b6315537b010b0226631550fb010e022663154d77011102256315"
                         "49f1011502246315466b01190223631542e5011d022163153f62011e022163153bde011e022163153859",
                         version=ns.version)
print(json.dumps(decoded, indent=4))
