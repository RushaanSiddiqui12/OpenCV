import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def rescaleFrame(frame, scale=2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Images/acat.jpg')
new = rescaleFrame(img)
cv.imshow('Cat', new)

blank = np.zeros(new.shape[:2], dtype='uint8')
# cv.imshow('Blank', blank)

gray = cv.cvtColor(new, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

mask = cv.circle(blank, (375,200), 100, 255, -1)
# cv.imshow('Mask', mask)
masked = cv.bitwise_and(gray, gray, mask=mask)
cv.imshow('Masked', masked)

gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])
plt.figure()
# plt.plot(gray_hist)
plt.title('Histogram Computation')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.xlim([0,256])
# plt.show()

colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)