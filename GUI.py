import tkinter
from tkinter import Canvas, ttk


class GUI:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Simple GUI")
        self.window.geometry("500x300")
        self.canvas = Canvas(self.window, width=500, height=300)
        #self.canvas.pack()
        self.column = tkinter.StringVar()
        self.columnentry = ttk.Entry(self.window, textvariable=self.column, width=30, background="white")
        self.columnentry.pack()
        self.column.trace_add("write", self.update)
    def update (self, *args):
        print(self.column.get())

    def run(self):
        self.window.mainloop()

