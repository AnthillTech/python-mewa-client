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

def notifyPropertyChanged(propertyName, value):
    return '{"message": "notify-property-changed", "property": "%s", "value": "%s"}' % (propertyName, value)

def setDeviceProperty(device, propertyName, value):
    return '{"message": "set-device-property", "device": "%s", "property": "%s", "value": "%s"}' % (device, propertyName, value)

def sendPropertyValue(device, propertyName, value):
    return '{"message": "send-property-value", "toDevice": "%s", "property": "%s", "value": "%s"}' % (device, propertyName, value)

def getDeviceProperty(device, propertyName):
    return '{"message": "get-device-property", "device": "%s", "property": "%s"}' % (device, propertyName)
