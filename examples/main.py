'''
Created on 27 lip 2014

@author: Krzysztof Langner
'''

from mewa.client import Connection


#HOST_URL = "ws://mewa.cc:9001/ws"
HOST_URL = "ws://localhost:9000/ws"

connection = Connection(HOST_URL)

def onConnected():
    connection.getDevices()
    connection.sendEvent("serviceA.event2", "78", True)
    params = [{"type": "org.fi24.switch", "name": "switch2"}, {"type": "org.fi24.switch", "name": "switch1"}, {"type": "org.fi24.switch", "name": "switch0"}]
    connection.sendMessage("device66", "serviceA.level", params)

def onEvent(timestamp, fromDevice, eventId, params):
    print("received event %s from %s with params %s" % (eventId, fromDevice, params))

def onMessage(timestamp, fromDevice, msgId, params):
    print(timestamp + ": received message %s from %s with params %s" % (timestamp, msgId, fromDevice, params))
    
def onDevicesEvent(timestamp, devices):
    print(timestamp + ": Found devices:")
    print(devices)
    
def onError(reason):
    print("Error: " + reason)
    
def onAck():
    print("ACK")
    

if __name__ == "__main__":
    connection.onConnected = onConnected
    connection.onEvent = onEvent
    connection.onMessage = onMessage
    connection.onDevicesEvent = onDevicesEvent
    connection.onError = onError
    connection.onAck = onAck
#     connection.connect("admin.test", "python", "l631vxqa")
    connection.connect("test", "python", "l631vxqa")



