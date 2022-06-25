import cv2 as cv

def rescaleImage(frame, scale=2.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# 1. Converting to gray scale

img = cv.imread('Images/city.jpg')
cv.imshow('city', img)
# new_img = rescaleImage(img)
# cv.imshow('new', new_img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# 2. Blurring

blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# 3. Edge cascading

canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

# 4. Dilating the image

dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilated)

# 5. Erodng

eroding = cv.erode(canny, (3,3), iterations=1)
cv.imshow('Eroding', eroding)

# 6. Cropping

cropped = img[50:200,50:200]
cv.imshow('Cropped', cropped)

cv.waitKey(0)