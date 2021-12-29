import os
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
a=Tk()

a.geometry("270x385")
a.title("Delete WA")

home = os.environ['HOME']
fpath = os.path.join(home, ".local/share/applications")
list_files = os.listdir(fpath)
check_for_files = [ file for file in list_files if 'webapp' in file ]

check_for_files_var = tk.StringVar(value=check_for_files)

def delete_wa():
  to_del = cfiles.curselection()
  selected_file = ",".join([cfiles.get(i) for i in to_del])
  delfile_loc = f"{fpath}/{selected_file}"
  os.remove(delfile_loc)
  del_btn.config(text = "Deleted!")
  label2.config(text = f"Deleted {selected_file}")

def exit():
  a.destroy()

def back():
  a.destroy()
  os.system('python3 /usr/bin/WebAppManager.py')

label1 = tk.Label(a, text = "WebApps created:").place(x=10,y=10)
label2 = tk.Label(a, text = "")
label2.place(x=10,y=290)

cfiles = tk.Listbox(a, width=33)
cfiles.place(y=40)
for entry in check_for_files:
  cfiles.insert(tk.END, entry)

del_btn = tk.Button(a, text = "Delete", command = delete_wa)
del_btn.place(x=98,y=250)

exit_btn = tk.Button(a, text = "Exit", command = exit).place(x=205,y=342)

back_btn = tk.Button(a, text = "Back", command = back).place(x=15,y=342)

a.mainloop()