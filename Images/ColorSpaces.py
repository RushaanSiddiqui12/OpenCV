import cv2 as cv 
import matplotlib.pyplot as plt

img = cv.imread('Images/city.jpg')
cv.resize(img, (1500,1500), interpolation=cv.INTER_AREA)
# cv.imshow('City', img)

new = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', new)

# plt.imshow(img)
plt.imshow(new)
plt.show()

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

# cv.waitKey(0)