'''
Created on 2014-07-30

@author: Krzysztof Langner
'''
import json

def connect(channel, device, password, prefixes):
    msg = {"type": "connect", "channel":channel, "device":device, "password":password, "listenTo": prefixes}
    return json.dumps(msg)

def disconnect():
    return '{"type": "disconnect"}'

def getDevices():
    return '{"type": "get-devices"}'

def sendEvent(eventId, params, ack=False):
    msg = {"type": "send-event", "id": eventId, "ack": ack, "params": json.dumps(params)}
    return json.dumps(msg)

def sendMessage(device, msgId, params):
    msg = {"type": "send-message", "device": device, "id": msgId, "params": json.dumps(params)}
    return json.dumps(msg)
