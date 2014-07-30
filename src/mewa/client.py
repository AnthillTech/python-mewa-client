'''
Created on 2014-07-30

@author: Krzysztof Langner
'''
from websocket import create_connection
from threading import Thread
from mewa import Protocol
import json


class Connection(object):
    '''
    API for connecting to Mewa server
    '''

    def __init__(self, url):
        ''' Establish web socket communication '''
        self._ws = create_connection(url)
        self._thread = Thread(target=self._run, args=()).start()

        
    def connect(self, channel, device, password):
        ''' Connect device to the channel '''
        self._send( Protocol.connect(channel, device, password) )
        
    def close(self):
        ''' Close connection '''
        self._send(Protocol.disconnect())
        
    def onConnected(self): 
        ''' Event send after client was connected to the channel '''
        print("Connected to the channel")
        
    def onError(self, reason):
        ''' Error message received from server '''
        print("Error: " + reason)
        
    def onDeviceJoinedChannel(self, name):
        ''' Some device joined channel '''
        print(name + " joined channel")

    def onDeviceLeftChannel(self, name):
        ''' Some device left channel '''
        print(name + " left channel")
        
    def setDeviceProperty(self, device, propertyName, value):
        ''' Set property on given device '''
        print("set device property")
#             msg = {message: "set-device-property", device: device, property: property, value: value}
#             _connection._sendMsg(msg);
        
    def onSetProperty(self, propertyName, value):
        ''' Received command to set property to given value '''
        print("on set property")
        
    def notifyPropertyChanged(self, propertyName, value):
        ''' Notify devices in channel that property changed '''
        print("notify property changed")
#             msg = {message: "notify-property-changed", property: property, value: value}
#             _connection._sendMsg(msg);
        
    def onPropertyChanged(self, device, propertyName, value):
        ''' Received notiication about property change '''
        print("on property changed")
        
    def getDeviceProperty(self, device, propertyName):
        ''' Set device property '''
        print("get device property")
#             msg = {message: "get-device-property", device: device, property: property}
#             _connection._sendMsg(msg);
        
    def onGetProperty(self, fromDevice, propertyName):
        ''' Received set property command '''
        print("on get property")
        
    def sendPropertyValue(self, device, propertyName, value):
        ''' Send property value to another device'''
        print("send property value")
#             msg = {message: "send-property-value", toDevice: device, property: property, value: value}
#             _connection._sendMsg(msg);
        
    def onPropertyValue(self, fromDevice, propertyName, value):
        ''' Received set property command '''
        print("on property value")
        
    def getDevices(self):
        ''' Get list of all connected to the channel devices '''
        self._send(Protocol.getDevices())
        
    def onDevicesEvent(self, devices):
        ''' Received set property command '''
        print("devices list:")
        print(devices)

        
    def _run(self, *args):
        ''' Run websocket client
        '''
        self._is_running = True
        while self._is_running:
            msg = self._ws.recv()
            self._on_message(msg)
        self._ws.close()
        print("Socket closed")
        
    def _send(self, msg):
        print("Send: " + msg)
        self._ws.send(msg)
        
    def _on_message(self, msg):
        event = json.loads(msg)
        if event['message'] == 'connected':
            self.onConnected()
        elif event['message'] == 'disconnected':
            self._is_running = False
        elif event['message'] == "joined-channel":
            self.onDeviceJoinedChannel(event["device"]);
        elif event['message'] == "left-channel":
            self.onDeviceLeftChannel(event["device"]);
        elif event['message'] == "set-property":
            self.onSetProperty(event["property"], event["value"]);
        elif event['message'] == "get-property":
            self.onGetProperty(event["fromDevice"], event["property"]);
        elif event['message'] == "property-value":
            self.onPropertyValue(event["device"], event["property"], event["value"]);
        elif event['message'] == "property-changed":
            self.onPropertyChanged(event["device"], event["property"], event["value"]);
        elif event['message'] == "devices-event":
            self.onDevicesEvent(event["devices"]);
        