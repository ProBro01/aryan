from time import time
import work
import pickle
from win10toast import ToastNotifier
import tkinter as tk
import os

def addWork(nameField, dateField, timeFieldMin, timeFieldsec, dateBox, workBox):
    workName = nameField.get()
    datepassed = dateField.get().split('/')
    timepassed = (timeFieldMin.get(), timeFieldsec.get())
    creatWork(workName, datepassed, timepassed, dateBox, workBox)
    nameField.delete(0, "end")
    dateField.delete(0, "end")
    timeFieldMin.delete(0, "end")
    timeFieldsec.delete(0, "end")

def creatWork(name, datepassed, timepassed, dateBox, workBox):
    w = work.work(name, int(timepassed[0]), int(timepassed[1]), int(datepassed[2]), int(datepassed[1]), int(datepassed[0]))
    path = f"C:\\todo\\{datepassed}+{name}.todo"
    with open(path, 'wb') as f:
        f.write(pickle.dumps(w))
    dateBox.insert(tk.END, "/".join(datepassed))
    workBox.insert(tk.END, name)
    ToastNotifier().show_toast(title="Added", msg=f"Work has been addded\n1. Name : {name}\n2. Date : {'/'.join(datepassed)}\n3. Time : {timepassed[0]}:{timepassed[1]}", threaded=True)


def distroywork(dateBox, workBox):
    selection = dateBox.curselection()
    filename = f"C:\\todo\\{dateBox.get(selection[0]).split('/')}+{workBox.get(selection[0])}.todo"
    os.remove(filename)
    dateBox.delete(selection[0])
    workBox.delete(selection[0])
    ToastNotifier().show_toast(title="Removed", msg=f"work has been deleted", threaded=True)