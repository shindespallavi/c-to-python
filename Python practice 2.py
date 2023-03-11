#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2

# Load Image
img = cv2.imread("lena.jpg")
# Create Image
img_processed = None

# Scaling Down the image
img_processed = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

# Display Image
cv2.imshow("img", img)
cv2.imshow("img_processed", img_processed)
# Waiting for a key to press
cv2.waitKey()


# In[ ]:




