import cv2
import numpy as np
from matplotlib import pyplot as plt

# 图像的形态学——最大轮廓提取


img = cv2.imread('opencv-logo.png')
cv2.imshow('input', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (11, 11), (-1, -1))

# 轮廓发现
out, contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
height, width = img.shape[:2]
index = 0
max = 0

for i in range(len(contours)):
    x, y, w, h = cv2.boundingRect(contours[i])
    # 不可能大于原图
    if h >= height or w >= width:
        continue
    # 找到最大的轮廓
    area = cv2.contourArea(contours[i])
    if area > max:
        max = area
        index = i

# 绘制轮廓关键点和轮廓
result = np.zeros(img.shape, dtype=np.uint8)
points = cv2.approxPolyDP(contours[index], 4, True)
cv2.drawContours(img, contours, index, (0, 0, 255), 1, 8)
cv2.drawContours(result, contours, index, (0, 0, 255), 1, 8)
print(points.shape)     # (25, 1, 2) 25个点
print(points)
for pts in points:
    cv2.circle(img, (pts[0][0], pts[0][1]), 2, (0, 255, 0), 2, 8, 0)
    cv2.circle(result, (pts[0][0], pts[0][1]), 2, (0, 255, 0), 2, 8, 0)

cv2.imshow("result", result)
cv2.imwrite("./result.png", result)
cv2.imshow("output", img)
cv2.imwrite("./output.png", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
