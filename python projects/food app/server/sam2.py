# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the window
win.geometry("700x350")

# Create a Listbox widget
lb=Listbox(win)
lb.pack(expand=True, fill=BOTH)

# Define a function to edit the listbox ite
def save():
   for item in lb.curselection():
      print("You have selected "+ str(item+1))

# Add items in the Listbox
lb.insert("end","item1","item2","item3","item4","item5")

# Add a Button To Edit and Delete the Listbox Item
ttk.Button(win, text="Save", command=save).pack()

win.mainloop()