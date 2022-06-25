import cv2 as cv

def rescaleFrame(frame, scale=0.4):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Video

capture = cv.VideoCapture('Images/vidcat2.mp4')
while True:
    isTrue, frame = capture.read()
    resized_frame = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Resized Video', resized_frame)  

    if cv.waitKey(20) & 0XFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()