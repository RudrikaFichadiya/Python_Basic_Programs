# 13 - October - 2018
# Program to implement checkbox demo using tkinter with python
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Program to implement Check Box")
window.geometry('350x200')
lbl = Label(window, text="Checkbox Demo",font=("Comic Sans MS Bold", 10))
lbl.grid(column=0, row=0)
chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text='PASCAL', var=chk_state)
chk.grid(column=0, row=1)
chk_state2 = BooleanVar()
chk_state2.set(False)
chk1 = Checkbutton(window, text='COBOL', var=chk_state2)
chk1.grid(column=0, row=2)


window.mainloop()
