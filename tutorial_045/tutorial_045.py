import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像的二值分析——凸包检测

def threshold_demo(image):
    dst = cv2.GaussianBlur(image, (3, 3), 0)
    gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    cv2.imshow('input', dst)
    cv2.imshow('gray', gray)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
    cv2.imshow('binary', binary)
    return binary


img = cv2.imread('test.jpg')

# 避免修改原图
img = img.copy()
binary = threshold_demo(img)

# 轮廓发现
out, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    # 对轮廓进行凹性检测, 返回 bool
    convex = cv2.isContourConvex(contours[i])

    # params: 传入轮廓, 返回凸包上的坐标
    points = cv2.convexHull(points=contours[i], returnPoints=True)
    total = len(points)
    for k in range(len(points)):
        x1, y1 = points[k % total][0]
        x2, y2 = points[(k+1) % total][0]
        cv2.circle(img, (x1, y1), 4, (255, 0, 0), 2, 8, 0)
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2, 8, 0)
    print(points)
    print("convex: ", convex)

cv2.imshow('contours-hull', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
