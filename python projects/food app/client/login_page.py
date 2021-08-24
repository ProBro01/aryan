import tkinter
from tkinter import messagebox
import json

def login_page():
	global logstatus
	logstatus = ''
	def send_auth():
		auth_dict = {}
		value_check = 0
		if (username_entry.get()).strip() == '':
			tkinter.messagebox.showinfo('ERROR!', 'No username!')
		else:
			auth_dict["username"] = (username_entry.get()).strip()
			value_check = value_check + 1
		if (password_entry.get()).strip() == '':
			tkinter.messagebox.showinfo('ERROR!', 'No password!')
		else:
			auth_dict["password"] = (password_entry.get()).strip()
			value_check = value_check + 1
		if (userID_entry.get()).strip() == '':	
			tkinter.messagebox.showinfo('ERROR!', 'No userID!')
		else:
			auth_dict["userID"] = (userID_entry.get()).strip()
			value_check = value_check + 1 
		print(auth_dict)
		userID_entry.delete(0, 'end')
		password_entry.delete(0, 'end')
		username_entry.delete(0, 'end')
		username_entry.focus()
		if value_check == 3:
			auth_dict = json.dumps(auth_dict)
			client_socket.send(auth_dict.encode('ascii'))
			msg = client_socket.recv(1024)
			global logstatus
			if msg == '1':
				tkinter.messagebox.showinfo('login', 'login successfull')
				logstatus = 'logsuccess'
				login_window.destroy()
			elif msg == '0':
				tkinter.messagebox.showinfo('login', 'login fail')
				logstatus = 'logfail'

	def send_reg_request():
		pass

	#creating the main window of the login page
	login_window = tkinter.Tk()
	login_window.title("LOGIN")
	login_window.geometry('550x250')
	#making the login lable
	main_lable = tkinter.Label(login_window, text='LOGIN', font=('Helvetica', 20, 'bold'))
	main_lable.grid(row=0, column=2)
	#making an username labelx
	username_label = tkinter.Label(login_window, text='Username: ', font=('Helvetica', 10))
	username_label.grid(column=1, row=1, padx=(30,0), pady=(15,0))
	#making an entry for the username
	username_entry = tkinter.Entry(login_window, width=60)
	username_entry.grid(column=2, row=1, padx=(10,0))
	#making a password label
	password_lable = tkinter.Label(login_window, text='Password: ', font=('Helvetica', 10))
	password_lable.grid(column=1, row=2, padx=(30,0), pady=(15,0))
	#making an entry for the password
	password_entry = tkinter.Entry(login_window, show='*', width=60)
	password_entry.grid(column=2, row=2, padx=(10,0))
	#making an userID label
	userID_label = tkinter.Label(login_window, text='UserID: ', font=('Helvetica', 10))
	userID_label.grid(column=1, row=3, padx=(30,0), pady=(15,0))
	#making an entry for the userID
	userID_entry = tkinter.Entry(login_window, width=60)
	userID_entry.grid(column=2, row=3, padx=(10,0))
	#making the button of login
	login_button = tkinter.Button(login_window, text="login", command=send_auth, font=('Helvetica',10))
	login_button.grid(column=2, row=4, columnspan=1, pady=(10,0))
	#making the button of registration
	registration_button = tkinter.Button(login_window, text='register', command=send_reg_request, font=('Helvetica', 10))
	registration_button.grid(column=1, row=4, columnspan=2, pady=(10,0))
	login_window.mainloop()
	return logstatus

stat = login_page()
print(stat)