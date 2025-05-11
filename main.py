# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter
import GUI

from Tools.scripts.summarize_stats import save_raw_data
from functools import partial
from tkinter import ttk
from tkinter import Canvas
def parsefile() -> list[float]:
    file = open("test2404.csv", "r")
    data = file.read()
    floats = []
    values = data.split(";")
    for value in values:
        floats.append(float(value))
    return floats

def displaywindow(floats: list[float]) -> None:
    window = tkinter.Tk()
    window.title("Simple GUI")
    window.geometry("500x300")
    canvas = Canvas(window, width=500, height=300)
    canvas.pack()
    previous_y = 0.0
    previous_x = 0.0

    for value in floats:
        canvas.create_line(previous_x, previous_y, previous_x+1, value)
        previous_y = value
        previous_x = previous_x+1

    window.mainloop()

def sum(x, y):
    return x + y

def print_hi(bighead):
    # Use a breakpoint in the code line below to debug your script.
    print(f'goodevening, {bighead}')  # Press Ctrl+8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharmhaha')
    #x = 1.5
    #y = 12.5
    #sum(x, y)
    #print(sum(x, y))
    #save = parsefile()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
    #displaywindow(save)
    gui = GUI.GUI()
    gui.run()

