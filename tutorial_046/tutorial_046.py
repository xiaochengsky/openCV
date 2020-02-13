import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像的二值分析——霍夫直线检测


img = cv2.imread('test.jpg')

# 避免修改原图
img = img.copy()


cv2.imshow('contours-hull', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
