import cv2 as cv 

img = cv.imread('Images/group3.jpg')
img = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Person', img) 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
print('No. of Faces = ', len(face_rect))

for (x,y,w,h) in face_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cv.imshow('Face Detected', img)

cv.waitKey(0)