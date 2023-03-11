#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2

CAM = 0 for video file
CAM = 1 for CSI camera (On board camera) (Not avillable on Jetson AGX Xavier)
CAM = 2 for USB camera
CAM = 2

'''
CSI Camera
Supported Resolution and FPS mode
2592 x 1944 FR=30.000000 CF=0x1109208a10 SensorModeType=4 CSIPixelBitDepth=10 DynPixelBitDepth=10
2592 x 1458 FR=30.000000 CF=0x1109208a10 SensorModeType=4 CSIPixelBitDepth=10 DynPixelBitDepth=10
1280 x 720 FR=120.000000 CF=0x1109208a10 SensorModeType=4 CSIPixelBitDepth=10 DynPixelBitDepth=10
'''

if CAM:
WIDTH = 1280
HEIGHT = 720
FPS = 120


def get_tegra_pipeline(width, height, fps):
    return ("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int){}, height=(int){}, format=(string)NV12, framerate=(fraction){}/1 ! nvvidconv flip-method=0 ! video/x-raw,width=(int){}, height=(int){}, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink".format(width, height, fps, width, height))
if CAM == 1:
# Onboard camera
# Define the gstream pipeline
pipeline = get_tegra_pipeline(WIDTH, HEIGHT, FPS)
print("Using pipeline: \n\t{}".format(pipeline))
input = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
elif CAM == 2:
# USB camera
input = cv2.VideoCapture(0)
else:
# video file
input = cv2.VideoCapture("cars.mp4")

Create image matrix
img = cv2.imread("cars.jpg")
img_prev = img.copy()

create vector points
points, points_prev = [], []
status = []
error = []

create point detector
detector = cv2.ORB_create()
keypoints = []

Read Image
input.read(img)

keypoints = detector.detect(img, None)
points = cv2.KeyPoint_convert(keypoints)

Copy Image
img_prev = img.copy()
points_prev = points

while True:
ret, img = input.read()


if not ret:
    break

# Calculates an optical flow for the given input
cv2.calcOpticalFlowPyrLK(img_prev, img, points_prev, points, status, error)

# Copy Image
img_prev = img.copy()

for i in range(len(points)):
    cv2.circle(img, tuple(points[i]), 3, (0, 0, int(cv2.norm(points_prev[i]-points[i])*20)), 3)

points_prev = points

# Display Image
cv2.imshow("img", img)

c = cv2.waitKey(1)

if c == 27: # 27 is ESC key code
    break
cv2.destroyAllWindows()
input.release()


# In[ ]:




