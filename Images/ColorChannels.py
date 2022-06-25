import cv2 as cv 
import numpy as np 

img = cv.imread('Images/city.jpg')
cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('City', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank', blank)

b,g,r = cv.split(img)
# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

cv.waitKey(0)