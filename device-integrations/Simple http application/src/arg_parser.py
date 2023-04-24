import argparse

cmdlineParser = argparse.ArgumentParser(description="Performs the e2e test complete.")
# Send protocol
cmdlineParser.add_argument("--decoder", metavar='<decoder>', dest="decoder", required=False,
                           choices=["x-logic-nbiot-pulse-meter"], default="no-decoder",
                           help="Decoder that will decoder device data.")

ns = cmdlineParser.parse_args()


def get_arg_parser():
    return ns
