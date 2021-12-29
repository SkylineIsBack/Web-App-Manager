import os
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
a=Tk()

a.geometry("270x400")
a.title("Create WA")

wname=tk.StringVar()
url=tk.StringVar()
browser=tk.StringVar()
browser.set("Select a browser")
mode=tk.StringVar()
mode.set("Select a mode")

def selecticon():
  global iconfile
  iconfile = askopenfilename(filetypes = [('Icons', '*.png')])
  icon_btn.config(text = iconfile)

def create():
  a = wname.get()
  b = url.get()
  c = browser.get()
  d = mode.get()
  e = iconfile
  home = os.environ['HOME']
  if c == "Google Chrome":
    if d == "Incognito":
      execline = f"google-chrome --app={b} --incognito"
    else:
      execline = f"google-chrome --app={b}"
  elif c == "Chromium":
    if d == "Incognito":
      execline = f"chromium --app={b} --incognito"
    else:
      execline = f"chromium --app={b}"
  elif c == "Brave":
    if d == "Incognito":
      execline = f"brave-browser --app={b} --incognito"
    else:
      execline = f"brave-browser --app={b}"
  elif c == "Edge":
    if d == "Incognito":
      execline = f"microsoft-edge --app={b} --inprivate"
    else:
      execline = f"microsoft-edge --app={b}"
  elif c == "Firefox":
    if d == "Incognito":
      execline = f"firefox --private-window {b} --profile {home}/.mozilla/firefox/webapp-profile"
    else:
      execline = f"firefox {b} --profile {home}/.mozilla/firefox/webapp-profile"
  else:
    print("Smth is wrong")
  fpath = os.path.join(home, ".local/share/applications")
  sfilename = f"{a}-webapp.desktop"
  with open(f"{fpath}/{sfilename}", 'w') as f:
       f.write("[Desktop Entry]\n")
       f.write("Type=Application\n")
       f.write("Encoding=UTF-8\n")
       f.write("Name=")
       f.write(a + '\n')
       f.write("Comment=A Web App\n")
       f.write("Exec=")
       f.write(execline + '\n')
       f.write("Icon=")
       f.write(e + '\n')
  os.chmod(f"{fpath}/{sfilename}",0o0775)
  create_btn.config(text ="Done")

def exit():
  a.destroy()

def back():
  a.destroy()
  os.system('python3 /usr/bin/WebAppManager.py')

list1 = ["Google Chrome", "Chromium", "Brave", "Edge", "Firefox"]
list2 = ["Normal", "Incognito"]

label1 = tk.Label(a, text = "Name:")
label1.grid(row=0,column=0,padx=10,pady=10)

wname_entry = tk.Entry(a, textvariable = wname)
wname_entry.grid(row=0,column=1,padx=5,pady=10)

label2 = tk.Label(a, text = "URL:")
label2.grid(row=1,column=0,padx=10,pady=10)

url_entry = tk.Entry(a, textvariable = url)
url_entry.grid(row=1,column=1,padx=5,pady=10)

label3 = tk.Label(a, text = "Browser:")
label3.grid(row=2,column=0,padx=10,pady=10)

browser_menu = tk.OptionMenu(a, browser, *list1)
browser_menu.grid(row=2,column=1,padx=5,pady=10)
browser_menu.config(width = 15)

label4 = tk.Label(a, text = "Mode:")
label4.grid(row=3,column=0,padx=10,pady=10)

mode_menu = tk.OptionMenu(a, mode, *list2)
mode_menu.grid(row=3,column=1,padx=5,pady=10)
mode_menu.config(width = 15)

label5 = tk.Label(a, text = "Icon:")
label5.grid(row=4,column=0,padx=10,pady=10)

icon_btn = tk.Button(a, text = "Select an icon", command = selecticon, width = 17)
icon_btn.grid(row=4,column=1,padx=5,pady=10)

create_btn = tk.Button(a, text = "Create", command = create)
create_btn.place(x=100,y=280)

exit_btn = tk.Button(a, text = "Exit", command = exit).place(x=205,y=357)

back_btn = tk.Button(a, text = "Back", command = back).place(x=15,y=357)

a.mainloop()