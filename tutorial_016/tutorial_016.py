import cv2
import numpy as np

# 图像自定义的仿射变换

img = cv2.imread("messi5.jpg")
cv2.imshow('input', img)
h, w = img.shape[:2]


src_point = np.float32([[50, 50], [200, 50], [50, 200]])
dst_point = np.float32([[10, 100], [200, 50], [100, 250]])

# 构建仿射变换矩阵 [2, 3]
M = cv2.getAffineTransform(src_point, dst_point)

dst = cv2.warpAffine(img, M, (w, h))
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

