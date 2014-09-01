'''
Created on 2014-07-30

@author: Krzysztof Langner
'''
from websocket import create_connection
from threading import Thread
from mewa import Protocol
import json
from mewa.service import URI_DISCOVERY_GETSERVICES, URI_DISCOVERY_SERVICELIST


class Connection(object):
    '''
    API for connecting to Mewa server
    '''

    def __init__(self, url):
        ''' Establish web socket communication '''
        self._ws = create_connection(url)
        self._thread = Thread(target=self._run, args=()).start()
        
    def connect(self, channel, device, password, services = []):
        ''' Connect device to the channel '''
        self._services = services
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
        
    def onDeviceJoinedChannel(self, timestamp, name):
        ''' Some device joined channel '''
        print(name + " joined channel")

    def onDeviceLeftChannel(self, timestamp, name):
        ''' Some device left channel '''
        print(name + " left channel")
        
    def sendEvent(self, eventId, params):
        ''' Send event to all devices '''
        self._send( Protocol.sendEvent(eventId, params) )
        
    def onEvent(self, timestamp, device, eventId, params):
        ''' Received command to set property to given value '''
        print("event received")
        
    def sendMessage(self, device, msgId, params):
        ''' Send message to specific device '''
        self._send( Protocol.sendMessage(device, msgId, params) )
        
    def onMessage(self, timestamp, device, msgId, params):
        ''' Received message from device.
            Supports service discovery.
         '''
        if  msgId == URI_DISCOVERY_GETSERVICES:
            self.sendMessage(device, URI_DISCOVERY_SERVICELIST, self._services)
        
    def getDevices(self):
        ''' Get list of all connected to the channel devices '''
        self._send(Protocol.getDevices())
        
    def onDevicesEvent(self, timestamp, devices):
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
        except Exception as e:
            self.onError(str(e))
        
    def _send(self, msg):
        self._ws.send(msg)
        
    def _on_message(self, msg):
        print(msg)
        event = json.loads(msg)
        if event['type'] == 'connected':
            self.onConnected()
        elif event['type'] == 'disconnected':
            self._is_running = False
        elif event['type'] == "joined-channel":
            self.onDeviceJoinedChannel(event["time"], event["device"]);
        elif event['type'] == "left-channel":
            self.onDeviceLeftChannel(event["time"], event["device"]);
        elif event['type'] == "event":
            self.onEvent(event["time"], event["device"], event["id"], self._parseParams(event["params"]));
        elif event['type'] == "message":
            self.onMessage(event["time"], event["device"], event["id"], self._parseParams(event["params"]));
        elif event['type'] == "devices-event":
            self.onDevicesEvent(event["time"], event["devices"]);
        else:
            self.onError(event["message"]);
            
    def _parseParams(self, params):
        try:
            if len(params) > 0:
                return json.loads(params)
            else:
                return {}
        except Exception as e :
            return str(e)
        