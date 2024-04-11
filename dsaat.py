import tkinter
from tkinter import *
from tkinter.ttk import *
from time import strftime

master=tkinter.Tk()
master.title("Dijital Saat")
label = Label(master,font=("Digital-7",240,''),background = 'red', foreground='yellow')

def time():
  string=strftime("%H:%M:%S ")
  label.config(text=string)
  label.after(1000,time)

label.pack(anchor='center')
time()

master.mainloop()