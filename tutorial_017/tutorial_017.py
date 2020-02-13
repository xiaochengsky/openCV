import cv2
import numpy as np

# 图像的透视变换

img = cv2.imread("messi5.jpg")
cv2.imshow('input', img)

src_point = np.float32([[56, 65], [340, 50], [50, 400], [340, 400]])
dst_point = np.float32([[0, 0], [340, 0], [0, 400], [340, 400]])

# 构建变换矩阵 [2, 3]
M = cv2.getPerspectiveTransform(src_point, dst_point)

dst = cv2.warpPerspective(img, M, (340, 400))
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

