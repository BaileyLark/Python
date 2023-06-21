import cv2 as cv 
import numpy as np

img = cv.imread('images\Bmth_webp.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
haar_cascade = cv.CascadeClassifier('haar.xml')

faces_rect = haar_cascade.detectMutliScale(gray, scaleFactor=1.1, minNeighbors=3)

cv.imshow('img', gray)
cv.waitKey(0) 
