import PIL.ImageGrab

image = PIL.ImageGrab.grab()
save_path = "C:\\Users\Gamer\Pictures\MySnapshot.jpg"
image.save(save_path)
image.show()