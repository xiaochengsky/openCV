import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像的形态学——开闭运算

img = cv2.imread('LinuxLogo.jpg')
cv2.imshow('input', img)

kernel = np.ones((5, 5), dtype=np.uint8)

# 开运算(先腐蚀后膨胀)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# 闭运算(先膨胀后腐蚀)
closig = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)


cv2.imwrite('opening.jpg', opening)
cv2.imwrite('closig.jpg', closig)
cv2.imshow('opening', opening)
cv2.imshow('closig', closig)

cv2.waitKey(0)
cv2.destroyAllWindows()
