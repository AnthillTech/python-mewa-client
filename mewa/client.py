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
        self._url = url
        
    def connect(self, channel, device, password, prefixes=[]):
        ''' Establish web socket communication
            Connect device to the channel '''
        try:
            self._ws = create_connection(self._url)
            self._thread = Thread(target=self._run, args=()).start()
            self._send( Protocol.connect(channel, device, password, prefixes) )
        except Exception as e:
            self.onError(str(e))
        
    def close(self):
        ''' Close connection '''
        self._send(Protocol.disconnect())
        
    def onConnected(self): 
        ''' Event send after client was connected to the channel '''
        pass
        
    def onError(self, reason):
        ''' Error message received from server '''
        print("Error: " + reason)
        
    def onDeviceJoinedChannel(self, timestamp, name):
        ''' Some device joined channel '''
        pass

    def onDeviceLeftChannel(self, timestamp, name):
        ''' Some device left channel '''
        pass
        
    def sendEvent(self, eventId, params, ack=False):
        ''' Send event to all devices '''
        self._send( Protocol.sendEvent(eventId, params, ack) )
        
    def onEvent(self, timestamp, device, eventId, params):
        ''' Received command to set property to given value '''
        pass
        
    def onAck(self):
        ''' Received acknowledge packet from server '''
        pass
        
    def sendMessage(self, device, msgId, params):
        ''' Send message to specific device '''
        self._send( Protocol.sendMessage(device, msgId, params) )
        
    def onMessage(self, timestamp, device, msgId, params):
        ''' Received message from device.'''
        pass
        
    def getDevices(self):
        ''' Get list of all connected to the channel devices '''
        self._send(Protocol.getDevices())
        
    def onDevicesEvent(self, timestamp, devices):
        ''' Received set property command '''
        pass

        
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
        elif event['type'] == "ack":
            self.onAck();
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
        