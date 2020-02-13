import cv2
import numpy as np

# 图像的平移操作

img = cv2.imread("messi5.jpg")
h, w = img.shape[:2]

# 设置平移矩阵
bias = 100
M = np.float32([[1, 0, bias], [0, 1, bias]])

# 获取平移图像
dst = cv2.warpAffine(img, M, (w, h), borderValue=(255, 0, 0))
cv2.imshow('input---dst', np.hstack([img, dst]))

cv2.waitKey(0)
cv2.destroyAllWindows()

