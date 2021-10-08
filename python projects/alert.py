import threading
import time
from win10toast import ToastNotifier
import os
import pickle
import work

global flag
flag = 0
notification_queue = {}

def notification_generator():
    while True:
        try:
            for key, value in notification_queue.items():
                ToastNotifier().show_toast(title="WORK", msg=f"{key} \nat {value}", threaded = True)
                time.sleep(6)
            notification_queue.clear()
        except Exception as e:
            print(e)

threading.Thread(target=notification_generator).start()

todoPath = r"C:\todo"
while True:
    for var in os.listdir(todoPath):
        try:
            var = var.split('.')
            if len(var) != 1:
                if var[1] == 'todo':
                    path = f"C:\\todo\\{var[0]}.{var[1]}"
                    with open(path, 'rb') as f:
                        myobj = pickle.load(f)
                        current_time = f"{time.strftime('%I')}:{time.strftime('%M')}:00"
                        if myobj.getTime() == current_time:
                            notification_queue[myobj.getName()] = myobj.getTime()
                            print(notification_queue)
        except Exception as e:
            print(e)
    time.sleep(20)
#i have to make the notification