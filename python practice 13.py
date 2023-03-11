#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2

CAM = 0 for video file
CAM = 1 for CSI camera (On board camera) (Not available on Jetson AGX Xavier)
CAM = 2 for USB camera
CAM = 2

CSI Camera
Supported Resolution and FPS mode
2592 x 1944 FR=30.000000 CF=0x1109208a10 SensorModeType=4 CSIPixelBitDepth=10 DynPixelBitDepth=10
2592 x 1458 FR=30.000000 CF=0x1109208a10 SensorModeType=4 CSIPixelBitDepth=10 DynPixelBitDepth=10
1280 x 720 FR=120.000000 CF=0x1109208a10 SensorModeType=4 CSIPixelBitDepth=10 DynPixelBitDepth=10
if CAM:
WIDTH, HEIGHT, FPS = 1280, 720, 120


def get_tegra_pipeline(width, height, fps):
    return f"nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int){width}, height=(int){height}, format=(string)NV12, framerate=(fraction){fps}/1 ! nvvidconv flip-method=0 ! video/x-raw,width=(int){width}, height=(int){height}, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink"
else:
WIDTH, HEIGHT, FPS = None, None, None

if CAM == 1:
# Onboard camera
# Define the gstream pipeline
pipeline = get_tegra_pipeline(WIDTH, HEIGHT, FPS)
print("Using pipeline: \n\t", pipeline)
input = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
elif CAM == 2:
# USB camera
input = cv2.VideoCapture(0)
else:
# Video file
input = cv2.VideoCapture("cars.mp4")

Create Image matrix
img_gray = None

create point detector
detector = cv2.ORB_create()

create vector keypoints
img_keypoints, obj_keypoints = [], []

Read input image
_, img = input.read()

Create Reference Image
if CAM != 0:
while True:
# Read Image
_, img = input.read()
dst = img.copy() # Copy camera image
if CAM == 2:
# Create rectangle for USB camera
rect = (290, 100, 100, 100)
else:
# Create rectangle for CSI camera
rect = (720, 320, 150, 100)
# display rectangle on Image
cv2.rectangle(dst, rect, (255, 0, 0), 1, 8, 0)
cv2.imshow("dst", dst)

c = cv2.waitKey(30)
if c == 114:
break
cv2.destroyWindow("dst")

Create Image matrix
_, obj = input.read()
if CAM == 2:
obj = obj[100:200, 290:390]
else:
obj = obj[320:420, 720:870]

obj_keypoints = detector.detect(obj, None)
obj = cv2.drawKeypoints(obj, obj_keypoints, None)

while True:
ret, img = input.read()
if not ret:
break


# In[ ]:




