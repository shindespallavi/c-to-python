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

# Generate image
cv2.imwrite("lena_sobel.png", dst)

# Load generated Image
new_img = cv2.imread("lena_sobel.png")
# Display image
cv2.imshow("Sobel - Simple Edge Detector", new_img)
# Waiting for a key to press
cv2.waitKey()


# In[ ]:




