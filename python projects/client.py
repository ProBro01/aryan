import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("requesting for connection")
client.connect(('127.0.0.1', 12345))
def printer():
    while True:
        print(client.recv(1024).decode('utf-8'))

def writer():
    global message
    while True:
        message = input()
        if(message == 'close'):
            t1.join()
            t2.join()
            client.close()
        print(client.send(message.encode("ascii")))

t1 = threading.Thread(target = printer, name = 'printer')
t2 = threading.Thread(target = writer, name = 'writer')
t1.start()
t2.start()

