    # 13 - October - 2018
#program to implement how to change Label according to Entry field data
import tkinter
from tkinter import *


window = Tk()
window.title("GUi_Demo_Tkinter_Python")
window.geometry('400x400')
lbl = Label(window, text="hello ")
lbl.grid(column=1,row=0)
txt = Entry(window, width=50)
txt.grid(column=1, row=1)

def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=1)
window.mainloop()
 
