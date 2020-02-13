import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像的锐化处理——Gauss-Laplacian(LOG)算子

img = cv2.imread('messi5.jpg', 0)
cv2.imshow('input', img)

log_mat = np.array([[-2, -4, -4, -4, -2], [-4, 0, 8, 0, -4], [-4, 8, 24, 8, -4], [-4, 0, 8, 0, -4], [-2, -4, -4, -4, -2]], dtype=np.float32)
log = cv2.filter2D(img, cv2.CV_16S, log_mat)
log = cv2.convertScaleAbs(log)

cv2.imshow('log', log)

cv2.waitKey(0)
cv2.destroyAllWindows()



