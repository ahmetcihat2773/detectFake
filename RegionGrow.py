import numpy as np
import cv2
from Preprocessing import Preprocessing 

class RegionGrow(object):
    def __init__(self):
        print("CONTINUE WITH HERE")



img = cv2.imread('./UTFVP/0007_6_3_120523-110018.png',cv2.CV_8U)
preprocessing = Preprocessing()
preprocessing.showImage(img,"Original Image")

otsu_img = preprocessing.apply_otsu(img)
preprocessing.showImage(otsu_img,"After OTSU Thresholding")

dila_img = preprocessing.apply_dilation(otsu_img,10)
preprocessing.showImage(dila_img,"After Dilation")

# TODO: Apply region growing.