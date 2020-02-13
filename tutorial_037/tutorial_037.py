import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像的 Otsu 二值化

img = cv2.imread('messi5.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('input', img)
cv2.imshow('gray', gray)

# threshold = 127, 基础二值化
ret_basic, binary_basic = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Otsu 二值化
ret_otsu, binary_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Otsu 二值化配合高斯滤波
# params:   输入图像, 高斯核, x, y方向标准差
blur = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow('blur', blur)
ret_gauss_otsu, binary_gauss_otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('binary_basic', binary_basic)
cv2.imshow('binary_otsu', binary_otsu)
cv2.imshow('ret_gauss_otsu', binary_gauss_otsu)

print('ret_basic: %d, ret_otsu: %d, ret_gauss_otsu: %d' % (ret_basic, ret_otsu, ret_gauss_otsu))

cv2.waitKey(0)
cv2.destroyAllWindows()



