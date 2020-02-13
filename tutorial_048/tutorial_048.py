import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像的形态学——腐蚀与膨胀操作
# 使用 numpy 和 cv 定义结构化元素的区别: 当需要定义 十字行/圆形/椭圆形 等形状的核, 用 cv 更为方便

img = cv2.imread('LinuxLogo.jpg')
cv2.imshow('input', img)

# np.array 定义结构元素
kernel_np = np.ones((5, 5), dtype=np.uint8)
erosion_np = cv2.erode(img, kernel_np, iterations=1)
dilation_np = cv2.dilate(img, kernel_np, iterations=1)

# cv2 定义结构元素
kernel_cv = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3), (-1, -1))
erosion_cv = cv2.erode(img, kernel_cv, None, (-1, -1), 1)
dilation_cv = cv2.dilate(img, kernel_cv, None, (-1, -1), 1)

cv2.imwrite('erosion_np.jpg', erosion_np)
cv2.imwrite('dilation_np.jpg', dilation_np)
cv2.imshow('erosion_np', erosion_np)
cv2.imshow('dilation_np', dilation_np)

cv2.imwrite('erosion_cv.jpg', erosion_cv)
cv2.imwrite('dilation_cv.jpg', dilation_cv)
cv2.imshow('erosion_cv', erosion_cv)
cv2.imshow('dilation_cv', dilation_cv)


cv2.waitKey(0)
cv2.destroyAllWindows()
