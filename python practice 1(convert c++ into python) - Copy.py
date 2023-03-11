#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2

# Load image from file
img = cv2.imread('lena.jpg')

# Check for invalid input
if img is None:
    exit()

# Display image
cv2.imshow('Lena', img)

# Convert color image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Save result
cv2.imwrite('lenaGray.jpg', gray_image)

# Load grayscale image and display it
img_gray = cv2.imread('lenaGray.jpg')
cv2.imshow('Lena_Gray', img_gray)

# Waiting for a key to be pressed
cv2.waitKey()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




