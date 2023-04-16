import tkinter as tk 
from tkinter import messagebox
from PIL import ImageTk, Image

root = tk.Tk()

# Frames
frame = tk.LabelFrame(root, text="Frame Name", padx=10, pady=10)


# Selection boxes
r = tk.IntVar()
tk.Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda:clicked(1))
tk.Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda:clicked(2))

# Message Boxes

def popup():
    #messagebox.showinfo("Title", "Message")
    response = messagebox.askquestion("Title", "Message")
tk.Button(root, text="Click Me", command=popup)

# Creating new window 

top = tk.Toplevel()


root.mainloop()