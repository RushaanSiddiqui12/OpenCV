import cv2 as cv
import os
import numpy as np 

people = []
for i in os.listdir('F:\OpenCV\Train'):
    people.append(i)

# print(people)

DIR = r'F:\OpenCV\Train'

features = []
labels = []

haar_cascade = cv.CascadeClassifier('haar_face.xml')


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            face_rect = haar_cascade.detectMultiScale(gray, 1.1, 3)
            
            for (x,y,w,h) in face_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training Done-----------------')

# print('Length of Features = ', len(features))
# print('Length of LAbels = ', len(labels))

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)