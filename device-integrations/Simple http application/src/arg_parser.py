import argparse

cmdlineParser = argparse.ArgumentParser(description="Performs the e2e test complete.")
# Send protocol
cmdlineParser.add_argument("--decoder", metavar='<decoder>', dest="decoder", required=False,
                           choices=["x-logic-nbiot-pulse-meter", "dragino-nmds120",
                                    "dragino-nse01", "dragino-nsph01", "dragino-nlms01",
                                    "dragino-n95s31b", "dragino-nds03a", "dragino-cpn01"], default="no-decoder",
                           help="Decoder that will decoder device data.")

cmdlineParser.add_argument("--version", metavar='<version>', dest="version", required=False, default=0,
                           help="Version of the decoder.")

ns = cmdlineParser.parse_args()


def get_arg_parser():
    return ns
