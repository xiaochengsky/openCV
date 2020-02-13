import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像的二值分析——轮廓近似

def threshold_demo(image):
    dst = cv2.GaussianBlur(image, (3, 3), 0)
    gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    cv2.imshow('input', dst)
    cv2.imshow('gray', gray)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
    cv2.imshow('binary', binary)
    return binary


img = cv2.imread('test.png')

# 避免修改原图
img = img.copy()
binary = threshold_demo(img)

# 轮廓发现
out, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    # 计算包围目标的最小矩形区域
    rect = cv2.minAreaRect(contours[i])
    cx, cy = rect[0]

    # epsilon 定义出原始轮廓(rect)到近似轮廓的差距(result)
    epsilon = 0.05 * cv2.arcLength(contours[i], True)
    result = cv2.approxPolyDP(contours[i], epsilon, True)
    vertexes = result.shape[0]
    cv2.putText(img, str(vertexes), (np.int32(cx), np.int32(cy)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))


cv2.imshow('contours-Approx', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
