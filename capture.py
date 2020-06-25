import cv2
import time
import numpy as np
import skimage
from skimage import io
a=0
video=cv2.VideoCapture(0)
while True:
    a=a+1
    check, frame =video.read()
    print(check)
    print(frame)

    #saving the feed as images to compare
    img=cv2.imread('frame.jpg', cv2.IMREAD_COLOR)
    cv2.imshow('image',frame)
    cv2.imwrite("frame.jpg" , frame)
    
    key=cv2.waitKey(1)
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows
