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
from mewa.client import Connection

connection = Connection("ws://mewa.cc/ws")

def onConnected():
    connection.getDevices()
    
def onDevicesEvent(devices):
    print("Found devices:")
    print(devices)
    

if __name__ == "__main__":
    connection.onConnected = onConnected
    connection.onDevicesEvent = onDevicesEvent
    connection.connect("test", "python", "pass")

```

## Redistributing
This code is distributed under BSD3 License. It may be freely redistributed, subject to the provisions of this license.
