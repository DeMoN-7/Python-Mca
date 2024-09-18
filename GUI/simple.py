import tkinter as tk




#to create window
root=tk.Tk()

#to give title to window
root.title("Basic")

# to provide size for window
root.geometry("350x300")


# change_color function that change the background color of window
def change_color():
    root.configure(bg="red")


# to add button in window 
button=tk.Button(root,text="Click Me",command=change_color)
button.pack(pady=10,padx=20)


root.mainloop()