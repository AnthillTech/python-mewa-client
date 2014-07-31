# pymewa

## About
This is Python library which simplifies connection to the [Channel Server](https://github.com/AnthillTech/mewa).

## Requirements

* [WebSocket client](https://github.com/liris/websocket-client)


## Instalation

```bash
pip install mewa
```


## Sample usage pattern

List all devices connected to the channel

```python
connection = Connection("ws://mewa.cc/ws")

def onConnected():
    connection.getDevices()
    connection.sendEvent("serviceA.event2", "78")
    connection.sendMessage("device66", "serviceA.level", "34")

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



```

## Redistributing
This code is distributed under BSD3 License. It may be freely redistributed, subject to the provisions of this license.
