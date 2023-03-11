#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2

#Create Image
img = None

#Video capturing from video files
input = cv2.VideoCapture('cars.mp4')

while True:
ret, img = input.read()
if not ret:
break


# Display video
cv2.imshow("img", img)
c = cv2.waitKey(30)

# Check if spacebar key is pressed
if c == 32:  # 32 is ASCII code for spacebar
    break
cv2.destroyAllWindows()


# In[ ]:




