import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像的自适应阈值二值化

img = cv2.imread('messi5.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('input', img)
cv2.imshow('gray', gray)

# threshold = 127, 基础二值化
ret, binary_basic = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# params:                   输入图像, 大于阈值取255, 获得阈值的方法(领域的均值), 二值化方法, 领域大小, 最终取值加常数C
binary_mean = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=11, C=2)

binary_gauss = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, blockSize=11, C=2)

cv2.imshow('binary_basic', binary_basic)
cv2.imshow('binary_mean', binary_mean)
cv2.imshow('binary_gauss', binary_gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()



