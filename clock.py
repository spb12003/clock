
from tkinter import *
from tkinter.ttk import *

from time import strftime

##from flask import Flask, render_template, request





##clock = Flask(__name__)

##@clock.route("/")
##@clock.route("/index")
##def index():


root = Tk()
root.title("Clock")

def time():
  string = strftime('%I:%M:%S %p')
  label.config(text=string)
  label.after(1000, time)



##I'm a bit confused how it is being implemented but I installed a font package, they are in Portfolio folder
label = Label(root, font = ("ds_digital bold", 80), background = "black", foreground = "white")
label.pack(anchor='center')
time()

mainloop()
    











