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


```python
connection = Connection("ws://mewa.cc/ws")

def onConnected():
    connection.getDevices()
    connection.sendEvent("serviceA.event2", "78")
    connection.sendMessage("device66", "serviceA.level", "34")

def onEvent(timestamp, fromDevice, eventId, params):
    print("received event %s from %s with params %s" % (eventId, fromDevice, params))

def onMessage(timestamp, fromDevice, msgId, params):
    print(timestamp + ": received message %s from %s with params %s" % (timestamp, msgId, fromDevice, params))
    
def onDevicesEvent(ts, devices):
    print("Found devices:")
    print(devices)
    
if __name__ == "__main__":
    connection.onConnected = onConnected
    connection.onEvent = onEvent
    connection.onMessage = onMessage
    connection.onDevicesEvent = onDevicesEvent
    connection.connect("test", "python", "pass")
```

## Redistributing
This code is distributed under BSD3 License. It may be freely redistributed, subject to the provisions of this license.
