'''
Created on 2014-07-30

@author: Krzysztof Langner
'''

def connect(channel, device, password):
    return '{"message": "connect", "channel":"%s", "device":"%s", "password":"%s"}' % (channel, device, password)

def disconnect():
    return '{"message": "disconnect"}'

def getDevices():
    return '{"message": "get-devices"}'

def sendEvent(eventId, params):
    return '{"message": "send-event", "id": "%s", "params": "%s"}' % (eventId, params)

def sendMessage(device, msgId, params):
    return '{"message": "send-message", "device": "%s", "id": "%s", "params": "%s"}' % (device, msgId, params)
