import numpy as np
from matplotlib import pyplot as plt 
import cv2

class Preprocessing():
    def __init__(self):
        print("PREPROCESSING STARTED")
    def showImage(self,img,title):            
        plt.figure(figsize=(5,5))
        plt.imshow(img)
        plt.title(title)
        plt.show()
    def apply_otsu(self,img):
        ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        return th2
    def apply_dilation(self,img,iterat):
        # Apply dilation : 
        kernel = np.ones((3,3),np.uint8)
        dilation = cv2.dilate(img,kernel,iterations = iterat)
        return dilation  


"""
plt.figure(figsize=(5,5))
plt.hist(img.ravel(),256,[0,256])
plt.title("Histogram Before Threshold")

# Adaptive Threshold
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,5)
plt.figure(figsize=(5,5))
plt.imshow(th3)
plt.show()

plt.figure(figsize=(5,5))
plt.hist(img.ravel(),256,[0,256])
plt.title("Histogram After Adaptive Threshold")
plt.show()

# Gaus Filter
blur = cv2.GaussianBlur(th3,(5,5),0)
plt.figure(figsize=(5,5))
plt.imshow(blur)
plt.show()
"""