import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()

img = ImageTk.PhotoImage(Image.open('C:/Users/Gamer/Documents/GitHub/Learning/Mar-23/images/mercury.png'))
img2 = ImageTk.PhotoImage(Image.open('C:/Users/Gamer/Documents/GitHub/Learning/Mar-23/images/venus.png'))
img3 = ImageTk.PhotoImage(Image.open('C:/Users/Gamer/Documents/GitHub/Learning/Mar-23/images/earth.png'))
img4 = ImageTk.PhotoImage(Image.open('C:/Users/Gamer/Documents/GitHub/Learning/Mar-23/images/mars.png'))
img5 = ImageTk.PhotoImage(Image.open('C:/Users/Gamer/Documents/GitHub/Learning/Mar-23/images/jupiter.png'))
img6 = ImageTk.PhotoImage(Image.open('C:/Users/Gamer/Documents/GitHub/Learning/Mar-23/images/saturn.png'))
img7 = ImageTk.PhotoImage(Image.open('C:/Users/Gamer/Documents/GitHub/Learning/Mar-23/images/uranus.png'))
img8 = ImageTk.PhotoImage(Image.open('C:/Users/Gamer/Documents/GitHub/Learning/Mar-23/images/neptune.png'))

image_list = [img, img2, img3, img4, img5, img6, img7, img8]

# define the object, open the image then set it.
lbl = tk.Label(image=img)
lbl.grid(row=0, column=0, columnspan=3)
image_number = 0

def update_image(index):
    global lbl
    global image_number

    if (image_number - index < 0):
        lbl.grid_forget()
        lbl = tk.Label(image=image_list[image_number + index])
        image_number =+ index
        lbl.grid(row=0, column=0, columnspan=3)

back_button = tk.Button(root, text="<<", command=lambda:update_image(-1))
forward_button = tk.Button(root, text=">>", command=lambda:update_image(1))
button_quit = tk.Button(root, text='Quit', command=root.quit)

back_button.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
forward_button.grid(row=1, column=2)
root.mainloop()