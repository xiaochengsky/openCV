import cv2
import numpy as np

# 图像的色彩空间转换

img = cv2.imread('opencv-logo.png')
cv2.imshow('image', img)

# BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# BGR to YUV
yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# BGR to YCrCb
Crcb = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)

cv2.imshow('hsv---yuv---Crcb', np.hstack(([hsv, yuv, Crcb])))

# 在 HSV 色彩空间下提取 img 的蓝色部分, 参照对照表
lower_blue = np.array([100, 43, 46])
upper_blue = np.array([124, 255, 255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)
res = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('mask', mask)
cv2.imshow('res', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
