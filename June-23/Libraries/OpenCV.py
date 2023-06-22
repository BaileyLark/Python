import cv2 as cv 
import numpy as np
#cv.VideoCapture(0) # Capture webcam 
#while True: 
    #isTrue, frame = capture.read() # returns each frame, checks if valid first


blank = np.zeros((400,400), dtype='unit8')
img = cv.imread('images\jameswebb.png')

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

b, g, r = cv.split(img)
merged = cv.merge([b,g,r])

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
nblur = cv.blur(img, (3, 3)) # breaks up small section in 3 by 3, computes average
mblur = cv.medianBlur(3) #same as blur but assumes 3,3 
bblur = cv.bilateralFilter(img, 3, 30, 30) #like blur gets pixels from further distance 
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
edge = cv.Canny(img, 125, 150) 
dilated = cv.dilate(edge, (3,3), iterations=1)
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cropped = img[50:200, 200:400]
translated = translate(img, 100, 100)
flip = cv.flip(img, 0) #0 vertical, #1 horizontal

cv.imshow("image", nblur)
cv.waitKey(0) 
