import socket
import threading
import json
import mysql.connect

class server_customer:
	def __init__(self, ip, port):
		self.ip = ip
		self.port = port
		self.server_addr = (ip, port)
		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client_list = {}
		self.database_authentication = mysql.connect(host='localhost', user='root', passwd='', database='food_app_database')
		self.database_auth_cursor = database_authentication.cursor()
		self.database_food = mysql.connect.connect(host='localhost', user='root')

	def start(self):
		'''
		start the server by binding the address
		'''
		try:
			self.server_socket.bind(self.server_addr)
			self.server_socket.listen()
			threading.Thread(target=self.accepting_connections).start()
		except Exception as e:
			print(e)

	def accepting_connections(self):
		client_socket, client_address = self.server_socket.accept()
		threading.Thread(target=self.client_handler, args=(client_socket, client_address)).start()

	def client_handler(self, client_socket, client_address):
		'''
		do the authentication of the client
		send the entities to the client
		recives the order from the client
		and send the order to the administrator
		'''
		if self.authentication(client_socket, client_address):
			answer = '1'#login
			client_socket.send(answer.decode('ascii'))
		else:
			answer = '0'#invalid	
			client_socket.send(answer.decode('ascii'))
		if answer == '1':
			food_fetching_query = "select name from food_table"
			self.database_auth_cursor.execute(food_fetching_query)
			food_result = self.database_auth_cursor.fetchall()
			for var in food_result:
				client_socket.send(var[0].encode('ascii'))


	def authentication(self, client_socket, client_address):
		'''
		recives the data in json format
		check the data in the database
		send true or false
		return to the client_handler
		'''
		client_socket.send('auth'.encode('ascii'))
		authentication_data = client_socket.recv(4096).decoded('ascii')
		authentication_data = json.loads(authentication_data)#converting the authentication string to the python dictionary
		auth_query_string = f"select name from auth_user where (username='{authentication_data['username']}' and password='{authentication_data[password]}') and userID='{authentication_data[userID]}'"	
		self.database_auth_cursor.execute(auth_query_string)
		result = self.database_auth_cursor.fetchall()
		if result == []:
			return False
		else:
			return True