import cv2
import numpy as np
from matplotlib import pyplot as plt

# 图像去水印/修复
# 去除 opencv-logo 中蓝色的环

img = cv2.imread('opencv-logo.png')
cv2.imshow('input', img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (100, 43, 46), (124, 255, 255))
cv2.imshow('mask', mask)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
cv2.dilate(mask, kernel, mask)
result = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
cv2.imshow('result', result)
cv2.imwrite('result.png', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
