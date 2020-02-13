import cv2
import numpy as np

# 图像 ROI 的提取与操作

img = cv2.imread('opencv-logo.png')
cv2.imshow('image', img)

# 获取 ROI
roi = np.copy(img[290:560, 300:600, :])
cv2.imshow('roi', roi)

# 修改 ROI
m_roi = np.copy(roi)
m_roi[:, :, 0] = 0
cv2.imshow('m_roi', m_roi)

# 提取 roi, 对应 opencv-logo 的蓝色圆环
src = cv2.imread('opencv-logo.png')
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (100, 43, 46), (124, 255, 255))
cv2.imshow('mask', mask)

extract = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('extract', extract)

cv2.waitKey(0)
cv2.destroyAllWindows()


