import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像的二值分析——轮廓外界矩形
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

# 避免修改原图
img = img.copy()
binary = threshold_demo(img)

# 轮廓发现
out, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    cv2.drawContours(img, contours, i, (0, 0, 255), 2, 8)
    # 计算包围目标的最小矩形区域
    rect = cv2.minAreaRect(contours[i])
    cx, cy = rect[0]
    # 获得包围矩形的四个顶点坐标
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
    cv2.circle(img, (np.int32(cx), np.int32(cy)), 2, (255, 0, 0), 2, 8, 0)

cv2.imshow('contours-Matrix', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
