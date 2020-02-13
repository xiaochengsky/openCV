import cv2
import numpy as np

# 图像的翻转操作
# 和旋转操作不同, 翻转后的图像尺寸和像素是没变化的,所以也不含有其它的操作(插值处理等)

img = cv2.imread("messi5.jpg")
cv2.imshow('input', img)
print(img.shape)

# 倒影翻转
dst1 = cv2.flip(img, 0)
cv2.imshow('dst1', dst1)
print(dst1.shape)

# 镜像翻转
dst2 = cv2.flip(img, 1)
cv2.imshow('dst2', dst2)
print(dst2.shape)

# 对角翻转
dst3 = cv2.flip(img, -1)
cv2.imshow('dst3', dst3)
print(dst3.shape)


cv2.waitKey(0)
cv2.destroyAllWindows()

