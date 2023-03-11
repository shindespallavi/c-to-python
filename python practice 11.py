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
if CAM == 1:
WIDTH = 1280
HEIGHT = 720
FPS = 120


def get_tegra_pipeline(width, height, fps):
    return "nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)" + str(width) + ", height=(int)" +            str(height) + ", format=(string)NV12, framerate=(fraction)" + str(fps) +            "/1 ! nvvidconv flip-method=0 ! video/x-raw,width=(int)" + str(width) + ", height=(int)" +            str(height) + ", format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink"
# Define the gstream pipeline
pipeline = get_tegra_pipeline(WIDTH, HEIGHT, FPS)
print("Using pipeline: \n\t", pipeline)
input = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
elif CAM == 2:
# USB camera
input = cv2.VideoCapture(0)

else:
# video file
input = cv2.VideoCapture("cars.mp4")

create image matrix
img = None
desc = None

create vector keypoints
keypoints = []

create keypoint detector
detector = cv2.ORB_create()

while True:
ret, img = input.read()
if not ret:
break

keypoints = detector.detect(img, None)

# Create circle at keypoints
for i in range(len(keypoints)):
    cv2.circle(img, (int(keypoints[i].pt[0]), int(keypoints[i].pt[1])), 2, (0, 0, 255), 1)

# Display Image
cv2.imshow("img", img)
c = cv2.waitKey(1)


if c == 27:  # 27 is ESC key code
    break
input.release()
cv2.destroyAllWindows()


# In[ ]:




