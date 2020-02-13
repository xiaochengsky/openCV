import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像的形态学——顶帽与黑帽
# 礼帽: 原始图像与其开运算后得到的图像差
# 黑帽: 原始图像进行闭运算后与原始图像本身的差

img = cv2.imread('LinuxLogo.jpg')
cv2.imshow('input', img)

kernel = np.ones((9, 9), dtype=np.uint8)

# 礼帽
topHat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# 黑帽
blackHat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imwrite('topHat.jpg', topHat)
cv2.imshow('topHat', topHat)

cv2.imwrite('blackHat.jpg', blackHat)
cv2.imshow('blackHat', blackHat)

cv2.waitKey(0)
cv2.destroyAllWindows()
