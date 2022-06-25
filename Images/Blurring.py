import cv2 as cv 

img = cv.imread('Images/city.jpg') 
cv.imshow('City', img)

# Average

average = cv.blur(img, (3,3))
cv.imshow('Average', average)

# Gaussian Blur

gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("Gaussian", gauss)

# Median Blur

median = cv.medianBlur(img, 3)
cv.imshow("Median", median)

# Bilateral

bilateral = cv.bilateralFilter(img, 20, 45, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)