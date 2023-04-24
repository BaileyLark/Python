import tkinter as tk 
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
import sqlite3

root = tk.Tk()

def click(event):
    myLabel = tk.Label(root, text="you clicked a button").pack()

my_menu = tk.Menu(root)
root.config(menu=my_menu)

file_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=...)

root.mainloop()