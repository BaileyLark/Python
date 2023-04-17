import tkinter as tk 
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog

root = tk.Tk()
root.geometry("500x500")

# Frames
frame = tk.LabelFrame(root, text="Frame Name", padx=10, pady=10)
#my_image = tk.ImageTK.PhotoImage(Image.open())

# Selection boxes
r = tk.IntVar()
tk.Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda:...)
tk.Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda:...)

# Message Boxes

def popup():
    #messagebox.showinfo("Title", "Message")
    response = messagebox.askquestion("Title", "Message")
tk.Button(root, text="Click Me", command=popup)

# Opening a file selection box
#root.filename = filedialog.askopenfilename(initialdir="C:/downloads", title="Select a File")

vertical = tk.Scale(root, from_=0, to=100, orient="horizontal")
vertical.pack()

# checkboxes 
var = tk.IntVar()
c1 = tk.Checkbutton(root, text="Check This Box", variable=var)

# Drop down boxes 
clicked = tk.StringVar()
options = [
    "item0",
    "item1",
    "item2",
]
clicked.set("item0")
drop = tk.OptionMenu(root, clicked, *options).pack()

root.mainloop()