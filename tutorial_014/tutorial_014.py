import cv2
import numpy as np

# 图像的旋转操作

img = cv2.imread("messi5.jpg")
cv2.imshow('input', img)
h, w = img.shape[:2]
print('img.shape: ', img.shape)

# 设置旋转参数: 旋转中心, 旋转角度, 旋转后的缩放因子
M = cv2.getRotationMatrix2D((w/2, h/2), 45, 0.6)

# 获取平移图像
dst = cv2.warpAffine(img, M, (2*w, 2*h))
cv2.imshow('dst', dst)
print('dst.shape: ', dst.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()

