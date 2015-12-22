#Get sample video from: https://mega.nz/#!NUtDiTgQ!xFRWP91fdwaoCShTGbVVKXP_sm6PF-pHt5VbNL_s1fE
import cv2
import numpy as np

#Initialize video capture. if an integer is passed instead of a string
#the video source with that index is used
video = cv2.VideoCapture('video.mpeg')		
flag = True

#Create window to visualize results

cv2.namedWindow('faces')

#Initialize face detector object

face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

 

#Main loop

while flag:

    #Load next frame

    flag, frame = video.read()

    #Convert frame to grayscale

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect faces as rectangles

    rects = face_detect.detectMultiScale(gray, scaleFactor=1.3, 

                                     minNeighbors=4, minSize=(30, 30), 

                                     flags = cv2.CASCADE_SCALE_IMAGE)

    #Copy frame for visualization

    img = frame.copy()

    green = (0, 255, 0)

    #For each detected face...

    for x1, y1, x2, y2 in rects:

        #Draw rectangle in duplicated image

        cv2.rectangle(img, (x1, y1), (x2+x1, y2+y1), green, 2)

    #Show in window

    cv2.imshow('faces', img)

    #Wait for keypress 

    key = cv2.waitKey(5)

    if key == 'q':

        flag = False

cv2.destroyAllWindows()

---------------------------------------------------------------------------
error                                     Traceback (most recent call last)
<ipython-input-3-33851846d07b> in <module>()
     13     flag, frame = video.read()
     14     #Convert frame to grayscale
---> 15     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     16     #Detect faces as rectangles
     17     rects = face_detect.detectMultiScale(gray, scaleFactor=1.3, 

error: /build/buildd/opencv-2.4.8+dfsg1/modules/imgproc/src/color.cpp:3737: error: (-215) scn == 3 || scn == 4 in function cvtColor



