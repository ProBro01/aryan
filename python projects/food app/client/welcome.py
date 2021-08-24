import tkinter
from tkinter.ttk import *
import time


class welcomewin:
    def __init__(self, text_t):
        self.window = tkinter.Tk()
        self.text_t = text_t
        self.window.title(self.text_t)
        self.window.geometry("890x500")
        photo = tkinter.PhotoImage(file = r'static\welcome_start_button.png')
        win_canvas = tkinter.Canvas(self.window, width=890, height=500)
        win_canvas.pack()
        win_canvas.create_image(0, 0, image=photo, anchor='nw')          
        start_btn = tkinter.Button(self.window, text='start', command=self.distroywin)
        self.window.config(bg='white')
        self.window.mainloop()
    def distroywin(self):
        self.window.destroy()
welcomewin('ONERKER')