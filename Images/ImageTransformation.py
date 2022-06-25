import cv2 as cv
import numpy as np

img = cv.imread('Images/city1.jpg')
img = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('City1', img)

# Translation

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x = shift left
# -y = shift up
# x = shift right
# y = shift down

trans = translate(img, 100, 100)
cv.imshow('Translated', trans)

# def rotate(img, angle, rotPoint=None):
#     (height, width) = img.shape[:2]

#     if rotPoint is None:
#         rotPoint = (width//2, height//2)
    
#     rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
#     dimensions = (width, height)

#     cv.warpAffine(img, rotMat, dimensions)

# rotated = rotate(img, 45)
# cv.imshow('Rotated', rotated)


cv.waitKey(0)