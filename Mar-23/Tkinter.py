import tkinter as tk 
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
import sqlite3

root = tk.Tk()

def click(event):
    myLabel = tk.Label(root, text="you clicked a button").pack()


myButton = tk.Button(root, text="Click Me", command=click)
myButton.bind("<Button-3>", click)
myButton.pack()

root.mainloop()