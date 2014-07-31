'''
Created on 27 lip 2014

@author: Krzysztof Langner
'''

from mewa.client import Connection

connection = Connection("ws://mewa.cc/ws")
# connection = Connection("ws://localhost:9000/ws")

def onConnected():
    connection.getDevices()
    connection.sendEvent("serviceA.event2", "78")
    connection.sendMessage("device66", "serviceA.level", "34")
#     connection.close()

def onEvent(fromDevice, eventId, params):
    print("received event %s from %s with params %s" % (fromDevice, eventId, params))

def onMessage(fromDevice, eventId, params):
    print("received message %s from %s with params %s" % (fromDevice, eventId, params))
    
def onDevicesEvent(devices):
    print("Found devices:")
    print(devices)

    
def onPropertyChanged(device, propertyName, value):
    print("Property %s on device %s was changed to %s" % (device, propertyName, value))
    

if __name__ == "__main__":
    connection.onConnected = onConnected
    connection.onEvent = onEvent
    connection.onMessage = onMessage
    connection.onDevicesEvent = onDevicesEvent
    connection.connect("test", "python", "pass")


