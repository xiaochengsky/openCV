import cv2
from matplotlib import pyplot as plt


# 图像梯度——Sobel算子
img = cv2.imread('opencv-logo.png', 0)
cv2.imshow('input', img)

# Parms: 输入图像, 数据类型, x方向求导阶数(<=2), y方向求导阶数(<=2), Sobel算子核
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

cv2.imshow('sobel_x', sobel_x)
cv2.imshow('sobel_y', sobel_y)

sobel = cv2.add(sobel_x, sobel_y, dtype=cv2.CV_16S)
sobel = cv2.convertScaleAbs(sobel)
cv2.imshow('sobel', sobel)

cv2.waitKey(0)
cv2.destroyAllWindows()



