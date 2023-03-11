#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2

# Load Image from file
img = cv2.imread("lena.jpg")

# Create another image
dst = None
# Sobel operation
dst = cv2.Sobel(img, cv2.CV_32F, 1, 1)

# Display Image
cv2.imshow("Sobel - Simple Edge Detector", dst/256)
# Waiting for a key to press
cv2.waitKey()


# In[ ]:




