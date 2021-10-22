#import modules--------------------------------------------------------------------
import os
import shutil
import tkinter as tk
from tkinter.filedialog import askdirectory

#global variables------------------------------------------------------------------
filepath = ""
static = "a"
ext = ".pdf"

#Button functions------------------------------------------------------------------
def file_path():
    """Open a file for editing."""
    global filepath
    path = askdirectory()
    window.title(f"Bulk Rename - {filepath}")
    filepath = path
    lbl_path2 = tk.Label(fr_buttons,text="Selected path: "+path)
    lbl_path2.grid(row=4,column=0, sticky="ew", padx=5, pady=5)
    
def rename_files():
    global static,ext
    static = txt_static.get()
    ext = txt_ext.get()
    loc=filepath+"/"
    out = loc+"renamed_"+static
    i=1
    if not os.path.exists(out):
        os.mkdir(out)
    for files in os.listdir(loc):
        if files.endswith(ext):
            if(i%10 == 0):
                lbl_done = tk.Label(fr_buttons,text=str(i) + " files renamed")
                lbl_done.grid(row=5,column=0, sticky="ew", padx=5, pady=5)
            
            shutil.copy2(loc+files,out+"/"+static+str(i)+ext)
            i = i+1
    lbl_done = tk.Label(fr_buttons,text="All files renamed in folder :"+ out)
    lbl_done.grid(row=5,column=0, sticky="ew", padx=5, pady=5)

#Create window----------------------------------------------------------------------
window = tk.Tk()
window.title("Bulk rename files")
window.rowconfigure(0, minsize=400, weight=1)
window.columnconfigure(0, minsize=400, weight=1)



fr_buttons = tk.Frame(window,relief=tk.RAISED, bd=1)
fr_rename = tk.Frame(window,relief=tk.RAISED, bd=1)

btn_path = tk.Button(fr_buttons, text="select folder", command=file_path)
btn_rename = tk.Button(fr_rename, text="Rename", command=rename_files)

txt_static = tk.Entry(fr_buttons)
txt_ext = tk.Entry(fr_buttons)

lbl_ext = tk.Label(fr_buttons, text="file extension, ex .pdf")
lbl_static = tk.Label(fr_buttons,text="static letter ex. P for P1,P2,P3")
lbl_path = tk.Label(fr_buttons,text="selected folder")

lbl_ext.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
lbl_static.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
lbl_path.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

txt_ext.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
txt_static.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

btn_path.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_rename.grid(row=0, column=0, sticky="ew", padx=5, pady=5)


fr_buttons.grid(row=0, column=0, sticky="ns")
fr_rename.grid(row=1, column=0, sticky="ns")

window.mainloop()