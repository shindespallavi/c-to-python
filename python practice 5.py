#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np

CSI_CAM = 0

if CSI_CAM:
WIDTH, HEIGHT, FPS = 1280, 720, 120
pipeline = f"nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int){WIDTH}, height=(int){HEIGHT}, format=(string)NV12, framerate=(fraction){FPS}/1 ! nvvidconv flip-method=0 ! video/x-raw,width=(int){WIDTH}, height=(int){HEIGHT}, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink"
print(f"Using pipeline: \n\t{pipeline}\n")
cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
else:
cap = cv2.VideoCapture(0)

while True:
ret, frame = cap.read()
if ret:
# Sobel Operation
dst = cv2.Sobel(frame, cv2.CV_8U, 1, 1)
# Write to output file
cv2.imwrite("cap_cam.png", dst)
# Read generated file
new_img = cv2.imread("cap_cam.png")
# Display image
cv2.imshow("new_img", new_img)
if cv2.waitKey(1) == ord('q'):
break

cap.release()
cv2.destroyAllWindows()


# In[ ]:




