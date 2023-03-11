#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2

#Load Image
img = cv2.imread('lena.jpg')

for i in range(1, 20, 2):
# Create Image matrix
img_blurred = cv2.blur(img, (i, i))
# Canny operation
img_processed = cv2.Canny(img_blurred, 100, 150)
# Display Image
cv2.imshow('img', img)
cv2.imshow('img_processed', img_processed)
cv2.imshow('img_blurred', img_blurred)
# Waiting for a key to press
cv2.waitKey()

cv2.destroyAllWindows()


# In[ ]:




