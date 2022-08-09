"""
Author: Haochen Yu
"""
from flask import Flask, render_template, Response, request, send_from_directory
# from camera import VideoCamera
import cv2
import os

# App Globals (do not edit)
app = Flask(__name__)
camera = cv2.VideoCapture(0)
@app.route('/')
def index():
    return render_template('index.html') #you can customze index.html here

def gen():  
    
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/live')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
