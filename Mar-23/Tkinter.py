import tkinter as tk 

root = tk.Tk()

def mouse_down():
    print("Clicked")


myButton = tk.Button(root, text="Click Me!", command=mouse_down, fg='white', bg='gray').pack()


root.mainloop()