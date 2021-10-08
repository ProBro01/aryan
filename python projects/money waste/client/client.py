import socket

class Client:
    def __init__(self, name, ip, port):
        self.name = name
        self.ip = ip
        self.port = port
        self.address = (self.ip, self.port)

    @classmethod
    def sendData(data):
        print(data)