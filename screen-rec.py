from win32api import GetSystemMetrics
import pyautogui
import cv2
import numpy
import time 

#getting the dimensions 
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

dimensions = (width,height)

#formatting the video in XVID(contains mp4 format)
format_of_video = cv2.VideoWriter_fourcc(*"XVID")

src = "C:\\Users\\Ultimate\\Videos\\Recordings\\firstVid.mp4v"
video = cv2.VideoWriter(src,format_of_video,30.0,dimensions)

#total video time start to end
start_time = time.time()
duration = 15
end_time = start_time + duration


#looping and collecting the screenshots and storing in an array
while True:
    img = pyautogui.screenshot()
    frame_1 = numpy.array(img)
    frame_color = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
    
    video.write(frame_color)
    current_time = time.time()
    if current_time > end_time :
        break
        
video.release()

print("Recorded")
