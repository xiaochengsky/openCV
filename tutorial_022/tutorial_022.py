import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像直方图的反向投影(一般都在 hsv 色彩空间下完成)

roi = cv2.imread('opencv-logo.png')
r_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
cv2.imshow('roi', roi)

# target = cv2.imread('messi5.jpg')             # 可做对照
target = cv2.imread('opencv-blue-logo.png')
t_hsv = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)
cv2.imshow('target', target)

# roi 直方图, 归一化
# 调整 Bins 的大小, 可在一定程度上完善反向投影的效果
roiHist = cv2.calcHist([r_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
cv2.normalize(roiHist, roiHist, 0, 255, cv2.NORM_MINMAX)

scale = 1
dst = cv2.calcBackProject([t_hsv], [0, 1], roiHist, [0, 180, 0, 256], scale)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()



