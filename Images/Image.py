import cv2 as cv 

# Image

img = cv.imread('Images/acat.jpg') # It converts the image into matrix of pixels.
cv.imshow('Cat', img) # It is used to get the output.
cv.waitKey(0)



