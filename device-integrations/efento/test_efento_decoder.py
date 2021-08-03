#!/usr/bin/env python3

import sys
import argparse
import json
import logging
import traceback
import efento_decoder

log = logging.getLogger(__name__)

TESTDATA = "0a06282c02403cf61001183c2217080110f48cf386062096042a0a000000000000000000002216080210f48cf3860620642a0a0000000000000000000028ed98f38606381a4001482582010f383637393937303331393539343133"

if __name__ == '__main__':
    log.debug("*** START ***")

    cmdlineParser = argparse.ArgumentParser(prog="test_efento_decoder.py",
                                            description="Decodes sensor payload.")

    cmdlineParser.add_argument("-loglevel", metavar='<loglevel>',
                               choices=["INFO", "WARN", "DEBUG"], default="INFO",
                               help="Log level.Possible values  are INFO, WARN, DEBUG.")

    cmdlineParser.add_argument("payload", nargs='*',
                               help="Payload")
    
    ns = cmdlineParser.parse_args()
    
    logging.basicConfig(force=True, level=ns.loglevel, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")                                

    log.debug("loglevel = %s" % (str(ns.loglevel)))
    log.debug("payload = %s" % (str(ns.payload)))

    exitCode = 0
            
    try:

        if not ns.payload or ns.payload[0] == "TESTDATA":
            payload = TESTDATA
        else:
            payload = ns.payload[0]

        d = efento_decoder.decode(payload)
        
        log.info(json.dumps(d, sort_keys=True, indent=4))

    except Exception as ex:
        log.error(str(ex))
        exitCode = 1
        traceback.print_exc()

    finally:
        log.debug("*** END OK ***")
        sys.exit(exitCode)
        

    