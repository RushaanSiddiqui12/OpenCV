import cv2 as cv 
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('blank', blank)

img = cv.imread('Images/city1.jpg')
img = cv.resize(img, (500,500), interpolation=cv.INTER_AREA) 
# cv.imshow('img', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)


canny = cv.Canny(gray, 125, 175)
cv.imshow('canny', canny)

blur = cv.GaussianBlur(canny, (3,3),cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

contours, hierarchies = cv.findContours(blur, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# print(len(contours), ' contours are present.')

ret, thresh = cv.threshold(blur, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

cv.drawContours(blank, contours, -1, (0,0,255),1)
cv.imshow('Contours drawn', blank)

cv.waitKey(0)