import cv2
import numpy as np
import threading

def view():
    cam = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    while True:
        check, frame = cam.read()
        if not check:
            raise ValueError("Couldn't load the frame")
        # Convert into grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(gray, (x, y), (x + w, y + h), (120), 2)
        # Display the output
        cv2.imshow('img', frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

def main():

    x = threading.Thread(target=view)
    x.start()
    print('hello')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
