import cv2 as cv 
import numpy as np
#cv.VideoCapture(0) # Capture webcam 
#while True: 
    #isTrue, frame = capture.read() # returns each frame, checks if valid first
 
img = cv.imread('images\jameswebb.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
edge = cv.Canny(img, 125, 150) 
dilated = cv.dilate(edge, (3,3), iterations=1)
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cropped = img[50:200, 200:400]

cv.imshow("image", cropped)
cv.waitKey(0) 
