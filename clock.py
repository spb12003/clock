import tkinter as tk
#from tkinter.ttk import *

from time import *
from datetime import datetime
from pytz import timezone


##create the GUI window, call it box
box = tk.Tk()

##set the size of the window 
box.geometry("1000x400")

##title for the box
box.title("Clocks Around the World")

#Create a Label at the top of the page
label = tk.Label(box, text="The Times Around the World! ", font=('Times New Roman', 40), background='orchid')
label.pack(fill='both')


#Create button frame, a grid for the buttons
buttonframe = tk.Frame(box)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)

#These buttons are in column two and display the clocks
btn1 = tk.Button(buttonframe, font=('ds_digital bold', 20), background='gray')
btn1.grid(row=0, column=1, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, font=('ds_digital bold', 20), background='gray')
btn2.grid(row=1, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, font=('ds_digital bold', 20), background='gray')
btn3.grid(row=2, column=1, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, font=('ds_digital bold', 20), background='gray')
btn4.grid(row=3, column=1, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, font=('ds_digital bold', 20), background='gray')
btn5.grid(row=4, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, font=('ds_digital bold', 20), background='gray')
btn6.grid(row=5, column=1, sticky=tk.W+tk.E)


#these buttons are in column 1 and display the locations
btn1_n = tk.Button(buttonframe, text='Local Time', font=('times new roman', 20), background='light sky blue')
btn1_n.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2_n = tk.Button(buttonframe, text='New York City, USA', font=('times new roman', 20), background='light sky blue')
btn2_n.grid(row=1, column=0, sticky=tk.W+tk.E)

btn3_n = tk.Button(buttonframe, text='Lisbon, Portugal', font=('times new roman', 20), background='light sky blue')
btn3_n.grid(row=2, column=0, sticky=tk.W+tk.E)

btn4_n = tk.Button(buttonframe, text='Kabul, Afganistan', font=('times new roman', 20), background='light sky blue')
btn4_n.grid(row=3, column=0, sticky=tk.W+tk.E)

btn5_n = tk.Button(buttonframe, text='Ho Ching Minh, Vietnam', font=('times new roman', 20), background='light sky blue')
btn5_n.grid(row=4, column=0, sticky=tk.W+tk.E)

btn6_n = tk.Button(buttonframe, text='Los Angeles, USA', font=('times new roman', 20), background='light sky blue')
btn6_n.grid(row=5, column=0, sticky=tk.W+tk.E)

buttonframe.pack(fill='both')



#Clocks for local time and 5 other citys around the world
time_format = '%I:%M:%S %p'

def time_local():
  local_time = datetime.now().strftime(time_format)

  btn1.config(text=local_time)
  btn1.after(1000, time_local)

time_local()


def time_ny():

  zone = 'America/New_York'
  ny_time = datetime.now(timezone(zone)).strftime(time_format)

  btn2.config(text=ny_time)
  btn2.after(1000, time_ny)

time_ny()


def time_Lis():

  zone = 'Europe/Lisbon'
  lis_time = datetime.now(timezone(zone)).strftime(time_format)

  btn3.config(text=lis_time)
  btn3.after(1000, time_Lis)

time_Lis()


def time_kabul():

  zone = 'Asia/Kabul'
  kabul_time = datetime.now(timezone(zone)).strftime(time_format)

  btn4.config(text=kabul_time)
  btn4.after(1000, time_kabul)

time_kabul()  


def time_hcm():

  zone = 'Asia/Ho_Chi_Minh'
  hcm_time = datetime.now(timezone(zone)).strftime(time_format)

  btn5.config(text=hcm_time)
  btn5.after(1000, time_hcm)

time_hcm()


def time_la():

  zone = 'America/Los_Angeles'
  la_time = datetime.now(timezone(zone)).strftime(time_format)

  btn6.config(text=la_time)
  btn6.after(1000, time_la)
  
time_la()  





box.mainloop()
