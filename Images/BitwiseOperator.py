import cv2 as cv 
import numpy as np 

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
cv.imshow('Rectangle', rectangle)

circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)
cv.imshow('Circle', circle)

# Bitwise_And

bit_and = cv.bitwise_and(rectangle, circle)
cv.imshow('bit_and', bit_and)

# Bitwise_Or

bit_or = cv.bitwise_or(rectangle, circle)
cv.imshow('bit_or', bit_or)

# Bitwise_XOR

bit_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bit_xor', bit_xor)

# Bitwise_Not

bit_not = cv.bitwise_not(rectangle)
cv.imshow('Not Rectangle', bit_not)

cv.waitKey(0)