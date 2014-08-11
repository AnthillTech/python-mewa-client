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
        
    def sendEvent(self, eventId, params):
        ''' Send event to all devices '''
        self._send( Protocol.sendEvent(eventId, params) )
        
    def onEvent(self, device, eventId, params):
        ''' Received command to set property to given value '''
        print("event received")
        
    def sendMessage(self, device, msgId, params):
        ''' Send message to specific device '''
        self._send( Protocol.sendMessage(device, msgId, params) )
        
    def onMessage(self, device, msgId, params):
        ''' Received message from device '''
        print("Message received")
        
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
        try:
            self._is_running = True
            while self._is_running:
                msg = self._ws.recv()
                self._on_message(msg)
            self._ws.close()
        except Exception:
            self.onError("exception")
        
    def _send(self, msg):
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
        elif event['message'] == "event":
            self.onEvent(event["device"], event["id"], self._parseParams(event["params"]));
        elif event['message'] == "message":
            self.onMessage(event["device"], event["id"], self._parseParams(event["params"]));
        elif event['message'] == "devices-event":
            self.onDevicesEvent(event["devices"]);
            
    def _parseParams(self, params):
        try:
            return json.loads(params)
        except Exception:
            return "error parsing params"
        