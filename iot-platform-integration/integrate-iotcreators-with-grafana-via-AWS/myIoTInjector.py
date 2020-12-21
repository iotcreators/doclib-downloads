LAMFUNC_NAME="myIoTInjector"
DATABASE = "myIoTDB"
TABLE = "myIoTTable"
DEFAULT_DEVICE_TYPE = "Data"

import traceback
import time
import json

import logging
log = logging.getLogger(LAMFUNC_NAME)
log.setLevel(logging.DEBUG)

import boto3
from botocore.config import Config

def decodeData(dataStr):
    '''
    Generic decoding function for devices which data shall be stored 
    as string and which doesn't require any decoding.
    '''
    d = {
        "deviceType" : "Generic.Data",
        "Data": dataStr
    }
    return d

def decodeHexData(hexString):
    '''
    Generic decoding function for devices which data is a 
    hex coded string. 
    '''
    s = bytes.fromhex(hexString).decode("utf-8")
    
    log.debug("PAYLOAD: as str: %s" % (s))
     
    d = {
        "deviceType" : "Generic.HexData",
        "Data": s
    }
    return d


def decodePikkertonXBS200(hexString):
    '''
    Decoding function for the hex encoded payload
    of XBS200 device from Pikkerton.
    '''
    s = bytes.fromhex(hexString).decode("utf-8")

    log.debug("PAYLOAD: %s" % (s))
        
    d = {
        "deviceType" : "Pikkerton.XBS200"
    }
    
    for e in json.loads(s):
        # Temperature 
        if "/3303/0/5700" == e["n"]:
            d["Temperature"] = float(e["v"])
        
        # Humidity 
        elif "/3304/0/5700" == e["n"]:
            d["Humidity"] = float(e["v"])

        # CO2 
        elif "/3325/2/5700" == e["n"]:
            d["CO2"] = float(e["v"])

    return d


def decodeSDI(hexString):
    '''
    Decoding function for the hex encoded payload
    of comfort sensor from IMBUILDING.
    '''
    a = bytearray.fromhex(hexString)
    type = a[0]
    version = a[1]
    
    if type == 1 and version == 1:
        d = {
            "deviceType"  : "IMBUILDING.Comfort",
            "status"      : a[8],
            "BatteryV"    : int.from_bytes(a[9:11], "big") / 100.,
            "Temperature" : int.from_bytes(a[12:14], "big") / 100.,
            "Humidity"    : int.from_bytes(a[14:16], "big") / 100.,
            "CO2"         : int.from_bytes(a[16:18], "big"),
            "Presence"    : "true" if a[18] > 0 else "false"
        }
        return d
        
    elif type == 2 and version == 4:
        d = {
            "deviceType"  : "IMBUILDING.PeopleCount",
            "status"      : a[8],
            "BatteryV"    : int.from_bytes(a[9:11], "big") / 100.,
            "CounterA"    : int.from_bytes(a[12:14], "big"),
            "CounterB"    : int.from_bytes(a[14:16], "big")
        }
        return d
       
    else:
        log.warn("Unsupported type %d and version %d" % (type, version))
        return None
        
def writeRecordToDB(client, deviceId, timestamp, data):
    '''
    Builds the records and writes them into the Timestream DB. 
    '''
    records = []

    dimensions = [
        {'Name': 'deviceId', 'Value': deviceId},
        {'Name': 'deviceType', 'Value': data["deviceType"]}
    ] 
     
    for e in [  ["CO2", "DOUBLE"], ["Temperature", "DOUBLE"], ["Humidity", "DOUBLE"], 
                ["Presence", "BOOLEAN"],["BatteryV", "DOUBLE"], ["CounterA", "BIGINT"], 
                ["CounterB", "BIGINT"], ["Data", "VARCHAR"]]:
        n = e[0]
        t = e[1]

        if n in data.keys():
            r = { 
                'Dimensions': dimensions, 
                'MeasureName': n, 
                'MeasureValue': str(data[n]), 
                'MeasureValueType': t, 
                'Time': str(timestamp)
            }
            records.append(r)

    log.debug("writting records for device %s to Timestream DB ..." % (deviceId))
    result = client.write_records(DatabaseName=DATABASE, TableName=TABLE, Records=records, CommonAttributes={}) 

def lambda_handler(event, context):
    '''
    Lambda functions main entry point.
    '''
    log.info("=> %s" % (LAMFUNC_NAME))

    log.debug(json.dumps(event, sort_keys=True, indent=4))

    try:
        ###
        # Get the device type from the header. With the device
        # type the decoding function can be selected.
        
        devType = DEFAULT_DEVICE_TYPE
        
        if "DeviceType" in event["headers"].keys():
            devType = event["headers"]["DeviceType"]
            devType = devType.strip() if devType else DEFAULT_DEVICE_TYPE

        log.debug("DeviceType: %s" % (devType))

        decodeFuncName = "decode%s" % devType
        if decodeFuncName not in globals().keys():
            log.warn("Decoding function %s does not exist!" % (decodeFuncName))
            decodeFuncName = decodeData
            
        decodeFunc = globals()[decodeFuncName]
        
        ###
        # Get the Impact reports from the request body
                
        s = event["body"] if "body" in event.keys() else "{}"
        
        # If not body don't do anything
        if not s or len(s) == 0:
            return {'statusCode': 204, 'body': "OK"}        
        
        log.debug("BODY = %s" % (str(s)))
        
        body = json.loads(s)

        if not "reports" in body.keys():
            return {'statusCode': 200, 'body': "no reports"}


        ###
        # Create Timestream session
                    
        session = boto3.Session()
        cfg = Config(read_timeout=20, max_pool_connections=5000, retries={'max_attempts': 10})
        client = session.client('timestream-write', config=cfg)
            
        ###
        # Process each report record 
        
        for rep in body["reports"]:
            log.debug("PAYLOAD: %s" % (rep["value"]))

            data = decodeFunc(rep["value"])
            
            if data:
                writeRecordToDB(client, rep["serialNumber"], rep["timestamp"], data)

        return {'statusCode': 204, 'body': "OK"}
        
    except Exception as ex:
        log.error("%s" % (str(ex)))
        traceback.print_exc()
        return {'statusCode': 400, 'body': "ERROR: %s" % (str(ex))}