import tkinter as tk
from File_organizer import organize_files

root = tk.Tk()
root.title("File Organizer")
root.geometry("600x600")
root.config(bg="#A9A9A9")

path_inp=tk.Entry(root,width=50)
path_inp.pack(padx=20,pady=30)


def sendPath():
    path=path_inp.get() # to take value from the input block 
    if path:
        organize_files(path)


button=tk.Button(root,text="Organize",command=sendPath)
button.pack(padx=10,pady=10)

root.mainloop()
