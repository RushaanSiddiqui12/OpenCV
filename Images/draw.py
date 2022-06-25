import cv2 as cv 
import numpy as np 

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank', blank)
# blank[100:300,200:500] = 0,255,0
# cv.imshow('Green', blank)


# Drawing a Rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness = -1)
cv.imshow('draw', blank)

# Drawing a Circle

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 50, (0,0,255), thickness = -1)
cv.imshow('circle', blank)

# Drawing Line

cv.line(blank, (0,0), (250,250), (255,255,255), thickness = 5)
cv.imshow('line', blank)

# Putting text

cv.putText(blank, 'Hello Everyone', (25,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), 2)
cv.imshow('text', blank)

cv.waitKey(0)
