import json

from src.arg_parser import get_arg_parser
from src.decoders.decoder_factory import get_decoder

ns = get_arg_parser()
decoder = get_decoder(ns.decoder)
decoded = decoder.decode("00730000016701180268500371000bffd8fc24048807bcf40115b50029c905021187060100070000",
                         version=ns.version)
print(json.dumps(decoded, indent=4))
