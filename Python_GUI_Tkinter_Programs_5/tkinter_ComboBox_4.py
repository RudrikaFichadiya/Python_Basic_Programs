# 13 - October - 2018
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Demo to display combobox in tkinter")
window.geometry('350x200')
lbl = Label(window, text="Combobox Demo",font=("Comic Sans MS Bold", 10))
lbl.grid(column=0, row=0)
combo = Combobox(window)
combo['values']= ("Select Date", 1,2,3,4,5, "Text")
combo.current(0)
combo.grid(column=0, row=1)
window.mainloop()
