import cv2
import numpy as np
from matplotlib import pyplot as plt

# 图像的二值分析——轮廓发现
# 1. 图像二值化(或 canny 检测)
# 2. 轮廓检测

def threshold_demo(image):
    dst = cv2.GaussianBlur(image, (3, 3), 0)
    gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    cv2.imshow('input', dst)
    cv2.imshow('gray', gray)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
    cv2.imshow('binary', binary)
    return binary


img = cv2.imread('detect_blob.png')
img = img.copy()
binary = threshold_demo(img)

# 轮廓发现
out, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    cv2.drawContours(img, contours, i, (0, 0, 255), 2, 8)

cv2.imshow('contours', img)

cv2.waitKey(0)
cv2.destroyAllWindows()



