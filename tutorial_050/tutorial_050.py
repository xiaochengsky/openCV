import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像的形态学——形态学梯度
# 得到的是前景物体的轮廓

img = cv2.imread('LinuxLogo.jpg')
cv2.imshow('input', img)

kernel = np.ones((5, 5), dtype=np.uint8)

# 基本梯度
gradient_basic = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# 外梯度
dilation = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel)
gradient_exteral = cv2.subtract(dilation, img)

# 内梯度
erosion = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel)
gradient_interal = cv2.subtract(img, erosion)


cv2.imwrite('gradient_basic.jpg', gradient_basic)
cv2.imshow('gradient_basic', gradient_basic)

cv2.imwrite('gradient_exteral.jpg', gradient_exteral)
cv2.imshow('gradient_exteral', gradient_exteral)

cv2.imwrite('gradient_interal.jpg', gradient_interal)
cv2.imshow('gradient_interal', gradient_interal)


cv2.waitKey(0)
cv2.destroyAllWindows()
