'''
Created on 27 lip 2014

@author: Krzysztof Langner
'''

from mewa.client import Connection
import time


#connection = Connection("ws://mewa.cc/ws")
connection = Connection("ws://localhost:9000/ws")

def onConnected():
    connection.getDevices()
    connection.sendEvent("serviceA.event2", "78")
    params = [{"type": "org.fi24.switch", "name": "switch2"}, {"type": "org.fi24.switch", "name": "switch1"}, {"type": "org.fi24.switch", "name": "switch0"}]
    connection.sendMessage("device66", "serviceA.level", params)
#     connection.close()

def onEvent(timestamp, fromDevice, eventId, params):
    print("received event %s from %s with params %s" % (eventId, fromDevice, params))

def onMessage(timestamp, fromDevice, msgId, params):
    print(timestamp + ": received message %s from %s with params %s" % (timestamp, msgId, fromDevice, params))
    
def onDevicesEvent(timestamp, devices):
    print(timestamp + ": Found devices:")
    print(devices)
    
def onError(reason):
    print("Error: " + reason)
    print("Reconnecting in 5 secons.")
    time.sleep(5)
    connection.connect("test", "python", "test")
    

if __name__ == "__main__":
    connection.onConnected = onConnected
    connection.onEvent = onEvent
    connection.onMessage = onMessage
    connection.onDevicesEvent = onDevicesEvent
    connection.onError = onError
    connection.connect("test", "python", "test")


