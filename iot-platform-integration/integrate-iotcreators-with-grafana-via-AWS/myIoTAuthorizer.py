import json

# Client systems which are allowed to inject data
CLIENTS = {
    "iotCreators.Starterkit": {"token":"d86zGcbpRcDiiWb8UQEBChrI1WYxDXRrJDVwfdsd"}
}

def buildPolicyDocument(effect, resource="arn:aws:execute-api:*:*:*"):
    return {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": "execute-api:Invoke",
                "Effect": effect,
                "Resource": resource
            }
        ]
    }
    
def lambda_handler(event, context):
    global CLIENTS
    returnValue = None
    
    try:
        auth = event["headers"]["authorization"]
        auth = auth.strip() if auth else ""
        print("*** AUTH: %s" % (auth))

        if len(auth) == 0:
            raise Exception("No authorization token defined in authorziation header.")

        fields = auth.split(":")
        
        if len(fields) != 2:
            raise Exception("Authorization format of \"%s\" is invalid." % (auth))
            
        client = fields[0].strip()
        token = fields[1].strip()

        if client not in CLIENTS.keys():
            raise Exception("Unknown client %s (auth=%s)" % (client, auth))
            
        if token != CLIENTS[client]["token"]:
            raise Exception("Invalid token %s for client %s (auth=%s)" % (token, client, auth))

        # Get the the addressed route
        routeArn = event["routeArn"] if "routeArn" in event.keys() else "arn:aws:execute-api:*:*:*" 
        print("*** ROUTEARN: %s" % (routeArn))

        returnValue = {"principalId":client, "policyDocument": buildPolicyDocument("Allow", routeArn)}
    
    except ValueError as err:
        print(err)
        returnValue = {"principalId":None, "policyDocument": buildPolicyDocument("Deny")}

    print("*** RETURN: ***\n%s" % (json.dumps(returnValue, indent=4)))

    return returnValue
    
    
