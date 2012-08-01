import sys
import socket
import string
import os

class BotBot:
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 6667
        self.NICK = 'ophanim'
        self.owner = 'angelicstrike'
        self.CHANNELS = ["#testarena"]
        self.SOCKET = socket.socket()
        self.LOG_FILE = 'ophanimLog.log'
        self.LINE_COUNT = 1
        self.LITERALS = 'ophanimLiterals.log'

    def connect(self):
        self.SOCKET.connect((self.HOST, self.PORT))
        self.SOCKET.setblocking(0)
        self.request('NICK ' + self.NICK)

    def addChannel(self, channel):
        if(channel[0] != '#'):
            channel = '#' + channel
        self.CHANNELS.append(channel)
            
    def log(self, output):
        if(output != ''):
            f = open(self.LOG_FILE, 'a')
            f.write(str(self.LINE_COUNT) + ': ' + output + '\n')
            f.close()
            self.LINE_COUNT += 1

    def joinChannels(self):
        for channel in self.CHANNELS:
            self.request('JOIN ' + channel)

    def request(self, request):
        self.log(request + '\n')
        self.SOCKET.send(bytes(request + '\n', "utf-8"))

    def response(self):
        try:
            buff = self.SOCKET.recv(500)
        except IOError:
            buff = b''            
        if(buff.strip() != ''):
            self.log((buff.strip()).decode("utf-8"))
        return buff 
    
    def addQuote(self, output):
        if(output != ''):
            f = open(self.LITERALS, 'a')
            f.close()
