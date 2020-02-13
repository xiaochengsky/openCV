import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像的二值分析——几何矩中心与横纵比过滤

def threshold_demo(image):
    dst = cv2.GaussianBlur(image, (3, 3), 0)
    gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    cv2.imshow('input', dst)
    cv2.imshow('gray', gray)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
    cv2.imshow('binary', binary)
    return binary


def canny_demo(image):
    threshold = 80
    canny = cv2.Canny(image, threshold, 2 * threshold)
    cv2.imshow('canny', canny)
    return canny

img = cv2.imread('opencv-logo.png')

# 避免修改原图
img = img.copy()
# binary = threshold_demo(img)
# canny 效果更好
binary = canny_demo(img)


# 轮廓发现
out, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    rect = cv2.minAreaRect(contours[i])
    # x, y, w, h
    cx, cy = rect[0]
    cw, ch = rect[1]

    mm = cv2.moments(contours[i])
    m00 = mm['m00']
    m01 = mm['m01']
    m10 = mm['m10']
    if m00 == 0:
        continue

    # 获取图像宽高比
    ratio = np.minimum(cw, ch) / np.maximum(cw, ch)
    print('the ' + str(i) + 'th ratio: %d' % ratio)

    # 重心
    cx = np.int(m10 / m00)
    cy = np.int(m01 / m00)

    # 最小外接矩形, 获得四个坐标
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    # 横纵比过滤
    # if ratio > 0.9:
    cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
    cv2.circle(img, (np.int32(cx), np.int32(cy)), 2, (255, 0, 0), 2, 8, 0)
    # if ratio < 0.5:
    #     cv2.drawContours(img, [box], 0, (255, 0, 255), 2)
    #     cv2.circle(img, (np.int32(cx), np.int32(cy)), 2, (0, 0, 255), 2, 8, 0)

cv2.imshow('contours-Moment', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
