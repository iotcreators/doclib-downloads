import json

from flask import Flask, request

from src.arg_parser import get_arg_parser
from src.decoders.decoder_factory import get_decoder

app = Flask("Simple http server")
ns = get_arg_parser()
decoder = get_decoder(ns.decoder)


@app.route('/response-tests', methods=["POST"])
def decode():
    decoded = {}
    try:
        body = json.loads(request.data)
        data_to_decode = body["reports"][0]["value"]
        decoded = decoder.decode(data_to_decode)
    except Exception as ex:
        print(f"Exception: {str(ex)}")
    finally:
        print(f"Decoded data: {json.dumps(decoded, indent=4)}")
        return f"OK", 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6000, threaded=True, debug=False)
