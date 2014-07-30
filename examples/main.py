'''
Created on 27 lip 2014

@author: Krzysztof Langner
'''

from mewa.client import Connection

connection = Connection("ws://mewa.cc/ws")

def onConnected():
    connection.getDevices()
#     connection.close()

    
def onDevicesEvent(devices):
    print("Found devices:")
    print(devices)
    

if __name__ == "__main__":
    connection.onConnected = onConnected
    connection.onDevicesEvent = onDevicesEvent
    connection.connect("test", "python", "pass")


