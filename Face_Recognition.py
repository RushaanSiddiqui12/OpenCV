import numpy as np
import cv2 as cv 
import os 

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = []
for i in os.listdir('F:\OpenCV\Train'):
    people.append(i)

# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'F:\OpenCV\Train\Mukesh Ambani\Dhwaj Sharma.jpg')
img = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in face_rect:
    face_roi = gray[y:y+h, x:x+w] 

    label, confidence = face_recognizer.predict(face_roi)
    print('Label = ', people[label], 'with a confidence of', confidence)

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,0,255), 2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

cv.imshow('Detected Face', img)

cv.waitKey(0)