import tkinter as tk 

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number)) 

def button_add():
    first_number = entry.get()
    global first_num
    first_num = int(first_number)
    entry.delete(0, tk.END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, first_num + int(second_number))


button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda:button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda:button_click(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda:button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda:button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda:button_click(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda:button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda:button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda:button_click(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda:button_click(0))

button_adder = tk.Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = tk.Button(root, text="=", padx=88, pady=20, command=button_equal)
button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=lambda:entry.delete(0, tk.END))


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_adder.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=3)
button_clear.grid(row=4, column=1, columnspan=3)
#Button_0 = tk.Button(root, text="Enter Name", command=mouse_down, fg='white', bg='gray')

root.mainloop()