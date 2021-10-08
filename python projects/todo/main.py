import os
import subprocess
import gui
import tkinter as tk
import shutil
import threading

def alertPlayer():
    subprocess.run('python C:\\todo\\alert.py', shell=True)

try:
    path = r"C:\todo"
    os.mkdir(path)
    shutil.copy("alert.py", "C:\\todo")
    shutil.copy("work.py", "C:\\todo")
    subprocess.run('reg add HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v todo /t REG_SZ /d "C:\\todo\\alert.py"')
    threading.Thread(target=alertPlayer).start()
except Exception as e:
    pass

window = tk.Tk()
app = gui.App(master=window)
app.mainloop()