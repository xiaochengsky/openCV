import cv2
import numpy as np

# 读取图像并拷贝
# 修改像素点并显示
# 分别创建纯 BGR 图像

img = cv2.imread('lena.jpg')
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)

src = np.copy(img)
src[:200, :200, 0] = 255
cv2.imshow('src', src)

b_img = np.zeros(src.shape, src.dtype)
b_img[:, :, 0] = 255
cv2.imshow('b_img', b_img)

g_img = np.zeros(src.shape, dtype=np.uint8)
g_img[:, :, 1] = 255
cv2.imshow('g_img', g_img)

r_img = np.zeros([512, 512, 3], src.dtype)
r_img[:, :, 2] = 255
cv2.imshow('r_img', r_img)

cv2.waitKey(0)
cv2.destroyAllWindows()


