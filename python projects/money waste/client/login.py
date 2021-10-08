import tkinter as tk
import tkfieldspecs
import client

def setAttribute(master, geo, title):
    '''
    set the attribute of the tkinter window
    geometry, title and resizablity
    '''
    master.geometry(geo)
    master.title(title)
    master.resizable(0, 0)

def getDetails():
    '''
    get the data from username and password field
    strip the input to remove the spaces
    check if the field is filled or empty 
    if filled print that data
    else not
    '''
    udata = usernameField.get()
    pdata = passwordField.get()
    if udata.strip() == '' or pdata.strip() == '':
        print("Field is Empty")
    else:
        client.Client.sendData()
    usernameField.delete(0, tk.END)
    passwordField.delete(0, tk.END)
    usernameField.focus_set()

loginwindow = tk.Tk()
setAttribute(loginwindow, "500x450", "Login")
tkfieldspecs.addLabel(loginwindow, 0, 0, text="LOGIN", size=25, pady=50)
tkfieldspecs.addLabel(loginwindow, 1, 0, text="Username", size=13, sticky=tk.W, padx=50)
usernameField = tkfieldspecs.addentry(loginwindow, 2, 0, size=20, padx=50)
usernameField.focus_set()
tkfieldspecs.addLabel(loginwindow, 3, 0, text="Password", size=13, sticky=tk.W, padx=50)
passwordField = tkfieldspecs.addentry(loginwindow, 4, 0, size=20, show='*', padx=50)
passwordField.focus_set()
loginButton = tkfieldspecs.addButton(loginwindow, 5, 0, text="Login", pady=(20, 10), sticky=tk.W, padx=(50, 50), command=getDetails)
loginwindow.mainloop()