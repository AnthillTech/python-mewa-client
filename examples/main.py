'''
Created on 27 lip 2014

@author: Krzysztof Langner
'''

from mewa.client import Connection

connection = Connection("ws://mewa.cc/ws")

def onConnected():
    connection.getDevices()
#     connection.close()
    

if __name__ == "__main__":
    connection.connect("test", "python", "pass")
    connection.onConnected = onConnected


