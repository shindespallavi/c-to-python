#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2

#Create Image matrix
img = None
dst = None

#Load video
input_video = cv2.VideoCapture("cars.mp4")

#generate video
output_video = cv2.VideoWriter(
"cars_sobel.avi",
cv2.VideoWriter_fourcc(*'XVID'),
30,
(int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH)),
int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
)

while True:
ret, img = input_video.read()
if not ret:
break


# Sobel Operation
dst = cv2.Sobel(img, cv2.CV_8U, 1, 1)

# Write to output file
output_video.write(dst)

# Display output
cv2.imshow("dst", dst)

c = cv2.waitKey(30) & 0xFF

# Check if space key is pressed
if c == ord(' '):
    break
input_video.release()
output_video.release()
cv2.destroyAllWindows()


# In[ ]:




