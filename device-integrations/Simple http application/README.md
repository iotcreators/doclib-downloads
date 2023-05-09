# Scope
This simple application is provided as an example of very simple http application endpoint, capable of decoding data coming from a variety of different decoders.

## Getting started
To start the application, you need to install the required dependencies first.

To install the dependencies, just issue
```bash
$ pip install -r requirements.txt
```
To run the software it is necessary to have a cassandra dbms running, in the root folder it is already present a cassandra instance that can be launched by just typing
```bash
$ python app.py --decoder <your_chosen_decoder> --version <optional_decoder_version>
```

#Supported decoders
The following devices are supported for decoding:
- "x-logic-nbiot-pulse-meter"
- "dragino-nmds120",
- "dragino-nse01"
- "dragino-nsph01"
- "dragino-nlms01"
- "dragino-n95s31b"
- "dragino-nds03a"
- "dragino-cpn01"

#Input data
The input data of the decoders is a ascii hex string representing the raw payload sent by the device, as forwarded by the iotcreators backend.