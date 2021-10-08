import tkinter as tk

def addentry(master, rw, cl, wdth=20, hgt=10, font="Georgia", size='15', show=None, pady=0, padx=0):
    e = tk.Entry(master, font=(f"{font} {size}"), show=show)
    e.grid(row = rw, column=cl, ipadx=wdth, ipady=hgt, padx=padx, pady=pady)
    return e

def addLabel(master, rw, cl, text="LABEL", font="Times", size='12', sticky=None, pady=0, padx=0):
    l = tk.Label(master, text=text, font=f"{font} {size}")
    l.grid(row=rw, column=cl, sticky=sticky, padx=padx, pady=pady)
    return l

def addButton(master, rw, cl, text='BUTTON', padx=0, pady=0, sticky=None, command=None):
    b = tk.Button(master, text=text, command=command)
    b.grid(row=rw, column=cl, padx=padx, pady=pady, sticky=sticky)
    return b