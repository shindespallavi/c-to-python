#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np

CSI_CAM = 0 # (On board camera) (Not available on Jetson AGX Xavier)

CSI Camera:
Supported Resolution and FPS mode
2592 x 1944 FR=30.000000 CF=0x1109208a10 SensorModeType=4 CSIPixelBitDepth=10 DynPixelBitDepth=10
2592 x 1458 FR=30.000000 CF=0x1109208a10 SensorModeType=4 CSIPixelBitDepth=10 DynPixelBitDepth=10
1280 x 720 FR=120.000000 CF=0x1109208a10 SensorModeType=4 CSIPixelBitDepth=10 DynPixelBitDepth=10
if CSI_CAM:
WIDTH = 1280
HEIGHT = 720
FPS = 120


def get_tegra_pipeline(width, height, fps):
    return (
        "nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int){}, height=(int){}, format=(string)NV12, "
        "framerate=(fraction){}/1 ! nvvidconv flip-method=0 ! video/x-raw, width=(int){}, height=(int){}, "
        "format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink"
    ).format(width, height, fps, width, height)
Create image matrix
img = None
dst = None

if CSI_CAM:
# Onboard camera
# Define the gstream pipeline
pipeline = get_tegra_pipeline(WIDTH, HEIGHT, FPS)
print("Using pipeline: \n\t", pipeline, "\n")
input = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
else:
# USB camera
input = cv2.VideoCapture(0)

Create Output file
output = cv2.VideoWriter(
"cap_cam.avi",
cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'),
30,
(
int(input.get(cv2.CAP_PROP_FRAME_WIDTH)),
int(input.get(cv2.CAP_PROP_FRAME_HEIGHT))
)
)

while True:
ret, img = input.read()
if not ret:
break
# Sobel Operation
dst = cv2.Sobel(img, cv2.CV_8U, 1, 1)


# Write output
output.write(dst)
# Display image
cv2.imshow("dst", dst)
c = cv2.waitKey(30)
# Wait for Esc key to press
if c == 27:
    break
Release resources
input.release()
output.release()
cv2.destroyAllWindows()


# In[ ]:




