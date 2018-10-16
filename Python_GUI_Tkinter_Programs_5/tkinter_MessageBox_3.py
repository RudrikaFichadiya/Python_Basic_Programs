# 13 - October - 2018
#Messagebox demo
#button demo
import tkinter
from tkinter import *

root = tkinter.Tk()

def HoorayCallBack():
    messagebox.showinfo("Hello!!!Python", "Hello!!!Python")

box = Button(root, text = "ClickMe!!!", command = HoorayCallBack)

box.pack()
box.place(bordermode=INSIDE, height = 100, width = 100)
root.mainloop()
