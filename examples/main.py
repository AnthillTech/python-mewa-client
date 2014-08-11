'''
Created on 27 lip 2014

@author: Krzysztof Langner
'''

from mewa.client import Connection


# connection = Connection("ws://mewa.cc/ws")
connection = Connection("ws://localhost:9000/ws")

def onConnected():
    connection.getDevices()
    connection.sendEvent("serviceA.event2", "78")
    params = [{"type": "com.followit24.service.switch", "name": "switch2"}, {"type": "com.followit24.service.switch", "name": "switch1"}, {"type": "com.followit24.service.switch", "name": "switch0"}]
    connection.sendMessage("device66", "serviceA.level", params)
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


