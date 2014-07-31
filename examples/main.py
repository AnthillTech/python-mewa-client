'''
Created on 27 lip 2014

@author: Krzysztof Langner
'''

from mewa.client import Connection

connection = Connection("ws://mewa.cc/ws")
# connection = Connection("ws://localhost:9000/ws")

def onConnected():
    connection.getDevices()
    connection.notifyPropertyChanged("level", "123")
#     connection.setDeviceProperty("device8", "heat", "34")
    connection.getDeviceProperty("device8", "level")
#     connection.close()

def onGetProperty(fromDevice, propertyName):
    connection.sendPropertyValue(fromDevice, propertyName, "444")


def onSetProperty(propertyName, value):
    print("set property %s to value %s" % (propertyName, value))


def onPropertyValue(fromDevice, propertyName, value):
    print("Received from %s: %s = %s" % (fromDevice, propertyName, value))

    
def onDevicesEvent(devices):
    print("Found devices:")
    print(devices)

    
def onPropertyChanged(device, propertyName, value):
    print("Property %s on device %s was changed to %s" % (device, propertyName, value))
    

if __name__ == "__main__":
    connection.onConnected = onConnected
    connection.onGetProperty = onGetProperty
    connection.onDevicesEvent = onDevicesEvent
    connection.onPropertyChanged = onPropertyChanged
    connection.onSetProperty = onSetProperty
    connection.onPropertyValue = onPropertyValue
    connection.connect("test", "python", "pass")


