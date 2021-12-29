import os
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
a=Tk()

a.geometry("320x210")
a.title("WebApp Manager")

def create_wa():
  a.destroy()
  os.system('python3 /usr/bin/WAM/WAM-create.py')

def delete_wa():
  a.destroy()
  os.system('python3 /usr/bin/WAM/WAM-delete.py')

def exit():
  a.destroy()

label1= tk.Label(a, text = "What do you want to do?")
label1.grid(row=0,column=0,padx=75,pady=10)

create_btn = tk.Button(a, text = "Create a WebApp", command = create_wa)
create_btn.grid(row=1,column=0,padx=75,pady=10)

delete_btn = tk.Button(a, text = "Delete a WebApp", command = delete_wa)
delete_btn.grid(row=2,column=0,padx=75,pady=10)

exit_btn = tk.Button(a, text = "Exit", command = exit, width = 14)
exit_btn.grid(row=3,column=0,padx=75,pady=10)

a.mainloop()