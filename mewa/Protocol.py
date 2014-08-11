'''
Created on 2014-07-30

@author: Krzysztof Langner
'''
import json

def connect(channel, device, password):
    msg = {"message": "connect", "channel":channel, "device":device, "password":password}
    return json.dumps(msg)

def disconnect():
    return '{"message": "disconnect"}'

def getDevices():
    return '{"message": "get-devices"}'

def sendEvent(eventId, params):
    msg = {"message": "send-event", "id": eventId, "params": json.dumps(params)}
    return json.dumps(msg)

def sendMessage(device, msgId, params):
    msg = {"message": "send-message", "device": device, "id": msgId, "params": json.dumps(params)}
    return json.dumps(msg)
