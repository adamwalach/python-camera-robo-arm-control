from __future__ import division

import io
import picamera
import cv2
import numpy
import urllib2
import time
import datetime

print "Start!"

while True:
    #Create a memory stream so photos doesn't need to be saved in a file
    stream = io.BytesIO()

    #Get the picture (low resolution, so it should be quite fast)
    #Here you can also specify other parameters (e.g.:rotate the image)
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)
        camera.capture(stream, format='jpeg')

    #Convert the picture into a numpy array
    buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

    #Now creates an OpenCV image
    image = cv2.imdecode(buff, 1)

    #Load a cascade file for detecting faces
    face_cascade = cv2.CascadeClassifier('/opt/face/opencv/haarcascades/haarcascade_frontalface_alt.xml')

    #Convert to grayscale
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    #Look for faces in the image using the loaded cascade file
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    print "Found "+str(len(faces))+" face(s), %s" % time.ctime()

    #Draw a rectangle around every found face
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)
        print "Size: " + str(w) + "," + str(h)
        print "Coordinates: " + str(x) + "," + str(y)
        url = "http://pi-v2.iot.ixa.pl:3000/api?servo="
        centerX=90 # servo center point
        rangeX=50 # servo range of movement
        pointX=x+(w/2)
        valX =  centerX - (rangeX * (( pointX / 320 )-0.5))

        centerY=30
        rangeY=50
        pointY=y+(h/2)

        valY=centerY - (rangeY * (( pointY / 240 )-0.5))
        print "Center point:"+ str(pointX) + "," + str(pointY)
        print "Servo: " + str(valX) + "," + str(valY)
        try:
            urllib2.urlopen(url+"h&value=" + str(int(valX)), timeout=1).read()
            urllib2.urlopen(url+"v&value=" + str(int(valY)), timeout=1).read()
        except:
            print "Unable to open url"
        time.sleep (0.5);
        print "-------------------------------------------"
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),(1,235), font, 0.7,(255,255,255),2)
    cv2.imwrite('./output/images/result.jpg',image)

    #Save the result image
    time.sleep (0.3);
