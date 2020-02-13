import cv2
import numpy as np

# 图像通道的合并与分离

img = cv2.imread('lena.jpg')
cv2.imshow('image', img)

b, g, r = cv2.split(img)
cv2.imshow('bgr', np.hstack([b, g, r]))

merge = cv2.merge([b, g, r])
cv2.imshow('merge', merge)

cv2.waitKey(0)
cv2.destroyAllWindows()


