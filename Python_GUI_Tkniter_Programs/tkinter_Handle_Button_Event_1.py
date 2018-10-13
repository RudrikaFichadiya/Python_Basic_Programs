# 13 - October - 2018
#Program to implement handle click event of button
import tkinter
from tkinter import *

window = Tk()
window.title("Python With GUI")
#set the window size
window.geometry('600x600')
#initialize lable with class
#set font and text
lbl = Label(window, text="Hello",font=("Comic Sans MS Bold", 20))
lbl.grid(column=0, row=0)


def clicked():
    lbl.configure(text="Button was clicked...!!!")
def clickedoff():
    lbl.configure(text="Button was again clicked...!!!")
    
btn = Button(window, text="Click Me", bg="black", fg="white", command=clicked, font=("Comic Sans MS Italic", 10))
btn.grid(column=0, row=1)
btn2 = Button(window, text="Click to Change", bg="green", fg="white", command=clickedoff, font=("Comic Sans MS Italic", 10))
btn2.grid(column=1, row=1)

window.mainloop()

''''''
