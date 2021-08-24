import tkinter
#import mysql.connector
#import json
#mydb = mysql.connector.connect(host="localhost", user='root', passwd='')
#mycursor = mydb.cursor()
#mycursor.execute('use onerker')
#username = input('Enter username: ')
#password = input('Enter password: ')
#query = f"select * from food where name='{username}' and password='{password}'"	
#mycursor.execute(query)
#result = mycursor.fetchall()
#if result == []:
#	print("not valid user!")
#mycursor.execute("update food set password='probro_0' where name='Divyansh'")
#else:
#	print("valid user!")
#	print("User info:",result)
#mycursor.execute('select name from food')
#for var in mycursor.fetchall():
#	print(var[0])
#	print(type(var[0]))

#mycursor.execute("update food set password=':)' where name='Sunita'")
#mydb.commit()

#x = '{ "name":"John", "age":30, "city":"New York"}'
#y = json.loads(x)
#print(y["name"])
# loads -- json string to python dictionary
#z = json.dumps(y)
#print(z)
# dumps -- python dictionary to json string

'''
we get list of tuple
and each tuple represent the single row in the database table
and the value in the tuple are according to the datatype stored in database table
'''


window = tkinter.Tk()
window.title('Welcome')
window.geometry('400x400')
window.resizable(False, False)
blue_frame = tkinter.Frame(window, height=400, width=100)
blue_frame.place(x=0, y=0)
#creating the canvas
w = tkinter.Canvas(blue_frame, width=100, height=400, bg='#52a8f2')
w.place(x=-2, y=0)
#crating the line in at the end of canvas
line_end = w.create_line(101, 0, 101, 400)
#creating a frame of login
login_frame = tkinter.Frame(window, height=400, width=300)
login_frame.place(x=100, y=0)
#creating a canvas in login frame
login_canvas = tkinter.Canvas(login_frame, width=220, height=360, bg='#ffffff',)
login_canvas.place(x=40, y=15)
#creating the round rectangle
up_line = login_canvas.create_line(20, 20, 200, 20)
left_line = login_canvas.create_line(20, 20, 20, 80)
right_line = login_canvas.create_line(200, 20, 200, 80)
down_line = login_canvas.create_line(20, 80, 200, 80)
#adding the text to the canvas
login_label = tkinter.Label(login_canvas, text='LOGIN', font=('Helvetica', 20, 'bold'), bg='white')
login_label.place(x=65, y=33)
#creating the username rectangle
username_rect = login_canvas.create_rectangle(35, 158, 195, 200)
#creating the username entry field
username_entry = tkinter.Entry(login_frame, bg='#000000', fg='#ffffff')
username_entry.place(x=80, y=180, width=150, height=30)
#creating the password rectangle
password_rect = login_canvas.create_rectangle(35, 228, 195, 270)
#creating the password entry field
password_entry = tkinter.Entry(login_frame, bg='#000000', fg='#ffffff', show='*')
password_entry.place(x=80, y=250, width=150, height=30)
#creating buttons for login and registeration
login_label = tkinter.Label(login_canvas, text='login')
login_label.place(x=0, y=300)
def pri(event):
	print("clicked")
login_label.bind('<Button-1>',pri)

window.mainloop()
