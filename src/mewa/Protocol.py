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
