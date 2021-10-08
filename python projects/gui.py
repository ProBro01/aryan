from win10toast import ToastNotifier
import tkinter as tk
import functionality
import os
import pickle

class App(tk.Frame):
    notifer = ToastNotifier()
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("todo")
        self.master.geometry("310x286")
        self.master.resizable(0, 0)
        self.date_box = None
        self.work_box = None
        self.add_button = None
        self.date_field()
        self.work_field()
        self.addButton()
        self.removeButton()
        self.showwork()

    @staticmethod
    def removeWork(dateBox, workBox):
        functionality.distroywork(dateBox, workBox)

    @staticmethod
    def addWork(root, dateBox, workBox):
        top = tk.Toplevel(root)
        top.geometry("400x150")
        top.title("Add work")
        workLable = tk.Label(top, text="Work")
        workLable.grid(row=0, column=0)
        workField = tk.Entry(top)
        workField.grid(row=0, column=1)
        dateLable = tk.Label(top, text="Date")
        dateLable.grid(row=1, column=0)
        dateField = tk.Entry(top)
        dateField.grid(row=1, column=1)
        timeLable = tk.Label(top, text="Time")
        timeLable.grid(row=2, column=0)
        timeFieldMin = tk.Spinbox(top, from_=0, to=24)
        timeFieldMin.grid(row=2, column=1)
        timeLablecolon = tk.Label(top, text=":")
        timeLablecolon.grid(row=2, column=2)
        timeFieldsec = tk.Spinbox(top, from_=0, to=60)
        timeFieldsec.grid(row=2, column=3)
        add = tk.Button(top, text="Add", command=lambda: functionality.addWork(workField, dateField, timeFieldMin, timeFieldsec, dateBox, workBox))
        add.grid(row=3, column=0)
        top.grab_set()

    def date_field(self):
        self.date_box = tk.Listbox(self.master, height=15, width=20)
        self.date_box.grid(row=0, column=0)

    def work_field(self):
        self.work_box = tk.Listbox(self.master, height=15, width=30)
        self.work_box.grid(row=0, column=1)

    def addButton(self):
        self.add_button = tk.Button(self.master, text="Add Work", command=lambda: App.addWork(self.master, self.date_box, self.work_box))
        self.add_button.grid(row=1,column=0)

    def removeButton(self):
        self.remove_button = tk.Button(self.master, text="Remove Work", command=lambda: App.removeWork(self.date_box, self.work_box))
        self.remove_button.grid(row=1, column=1)

    def showwork(self):
        path = "C:\\todo"
        for var in os.listdir(path):
            var = var.split('.')
            if len(var) != 1:
                if var[1] =='todo':
                    file = f"C:\\todo\\{var[0]}.{var[1]}"
                    with open(file, 'rb') as f:
                        myobj = pickle.load(f)
                        self.date_box.insert(tk.END, myobj.getDate())
                        self.work_box.insert(tk.END, myobj.getName())