
import efento_proto_measurements_pb2 as proto_measurements_pb2
from google.protobuf.json_format import MessageToDict

def decode(payload):
    d = {}
    
    d1 = MessageToDict(proto_measurements_pb2.ProtoMeasurements.FromString(bytes.fromhex(payload)))

    if "channels" not in d1.keys():
        return None

    for e in d1["channels"]:
        if "type" not  in e.keys():
            continue
        
        if e["type"] == "MEASUREMENT_TYPE_TEMPERATURE":
            d["Temperature"] = e["startPoint"] / 10.
        elif e["type"] == "MEASUREMENT_TYPE_HUMIDITY":
            d["Humidity"] = e["startPoint"]

    d["Data"] = payload
    
    return d




    
