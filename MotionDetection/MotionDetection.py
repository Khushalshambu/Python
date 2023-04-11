from datetime import datetime
from encodings.utf_8 import getregentry
from tkinter import Frame
import cv2
from cv2 import filterHomographyDecompByVisibleRefpoints
from numpy import imag
import time
import pandas

camera_port = 0
camera = cv2.VideoCapture(camera_port,cv2.CAP_DSHOW)
framerate = 1
first_frame = None
status_list=[None,None]
times=[]
df= pandas.DataFrame(columns=["Start","End"])

frames = 120
while True:
    #start_time = time.time()
    framerate= framerate+1
    # time.sleep(4)
    read,frame = camera.read()
    status=0
    #print(read)
    #print(frame)

    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    grey= cv2.GaussianBlur(grey,(21,21,),0)

    #this line of code is to assign the first frame to the variable first frame
    if first_frame is None:
        first_frame=grey
        continue

    #line of code to take delta frame
    delta_frame = cv2.absdiff(first_frame,grey)

    #line for threshold frame
    threshold_frame = cv2.threshold(delta_frame,25,255,cv2.THRESH_BINARY)[1]

    threshold_frame=cv2.dilate(threshold_frame,None,iterations=2)

    (counts,_) = cv2.findContours(threshold_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in counts:
        if cv2.contourArea(contour) < 20000:
            continue
        status=1
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    status_list.append(status)

    status_list=status_list[-2:]
    if status_list[-1] == 1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2]==1:
        times.append(datetime.now())

    #line to show the output
    cv2.imshow("deltaframe",delta_frame)
    cv2.imshow("grey",grey)
    cv2.imshow("thresholdframe",threshold_frame)
    cv2.imshow("contourframe",frame)

    
    key = cv2.waitKey(1)

    #this is to break the code and stop the video
    if key == ord("x"):
        if status==1:
            times.append(datetime.now())
        break

print(status_list)
print(times)
for i in range(0,len(times),2):
    df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)

df.to_csv("Times.csv")
    


print(framerate)
camera.release()
cv2.destroyAllWindows()