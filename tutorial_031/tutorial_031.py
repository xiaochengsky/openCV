import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像 canny 边缘检测
img = cv2.imread('messi5.jpg', 0)

# params:           输入图像,   (NMS的)maxVal,   minVal,         通道设置,   Sobel算子核,       梯度计算方法
edges = cv2.Canny(image=img, threshold1=100, threshold2=200, edges=None, apertureSize=3, L2gradient=False)

cv2.imshow('input', img)
cv2.imshow('canny', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()



