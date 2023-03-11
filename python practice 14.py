#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2

CAM = 1 # 0 for video file, 1 for CSI camera, 2 for USB camera

# Supported resolution and FPS mode for CSI Camera
# 2592 x 1944 FR=30.000000 CF=0x1109208a10 SensorModeType=4 CSIPixelBitDepth=10 DynPixelBitDepth=10
# 2592 x 1458 FR=30.000000 CF=0x1109208a10 SensorModeType=4 CSIPixelBitDepth=10 DynPixelBitDepth=10
# 1280 x 720 FR=120.000000 CF=0x1109208a10 SensorModeType=4 CSIPixelBitDepth=10 DynPixelBitDepth=10

if CAM:
    WIDTH = 1280
    HEIGHT = 720
    FPS = 120

    # Define the gstream pipeline
    pipeline = f"nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int){WIDTH}, height=(int){HEIGHT}, format=(string)NV12, framerate=(fraction){FPS}/1 ! nvvidconv flip-method=0 ! video/x-raw,width=(int){WIDTH}, height=(int){HEIGHT}, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink"
    print(f"Using pipeline: \n\t{pipeline}\n")
    input = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
    print("Press R key to take reference image")
else:
    input = cv2.VideoCapture("cars.mp4")

# Create Image matrix
img = None
img_gray = None
dst = None

# Create point detector
detector = cv2.ORB_create()
# Set max features
detector.setMaxFeatures(500)
# Create vector keypoints
img_keypoints, obj_keypoints = [], []
# Create Image matrix
img_descriptors, obj_descriptors = None, None
retval, img = input.read()

# Create Reference Image
if not CAM:
    while True:
        # Read Image
        retval, img = input.read()
        dst = img.copy()  # Copy camera image
        # Create rectangle for CSI camera
        rect = (720, 320, 150, 100) if CAM else (290, 100, 100, 100)
        # display rectangle on Image
        cv2.rectangle(dst, rect, (255, 0, 0), 1, 8, 0)
        cv2.imshow("dst", dst)
        # Note: To capture Reference image Press r key
        c = cv2.waitKey(30)
        # Wait for r key to press
        if c == ord('r'):
            break
    cv2.destroyWindow("dst")

# Create Image matrix
obj = None
# Crop image
if CAM == 2:
    obj = img[100:200, 290:390].copy()
else:
    obj = img[320:420, 720:870].copy()

# Detect keypoints and compute the descriptors
obj_keypoints, obj_descriptors = detector.detectAndCompute(obj, None)
img = cv2.drawKeypoints(obj, obj_keypoints, img)

while True:
    retval, img = input.read()
    if not retval:
        break
    # Detect keypoints and compute the descriptors
    img_keypoints, img_descriptors = detector.detectAndCompute(img, None)
    img = cv2.drawKeypoints(img, img_keypoints, img)


# In[ ]:




