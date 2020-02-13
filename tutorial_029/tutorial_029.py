import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像梯度——Scharr, robert, prewitt, Laplacian算子
img = cv2.imread('opencv-logo.png', 0)
cv2.imshow('input', img)

# Scharr
scharr_x = cv2.Scharr(img, ddepth=cv2.CV_16S, dx=1, dy=0)
scharr_y = cv2.Scharr(img, ddepth=cv2.CV_16S, dx=0, dy=1)
scharr_x_abs = cv2.convertScaleAbs(scharr_x)
scharr_y_abs = cv2.convertScaleAbs(scharr_y)
scharr = cv2.addWeighted(src1=scharr_x_abs, alpha=0.5, src2=scharr_y_abs, beta=0.5, gamma=0)


# robert
robert_x = np.array([[1, 0], [0, -1]], dtype=np.float32)
robert_y = np.array([[0, -1], [1, 0]], dtype=np.float32)
robert_grad_x = cv2.filter2D(img, cv2.CV_16S, robert_x)
robert_grad_y = cv2.filter2D(img, cv2.CV_16S, robert_y)
robert_grad_x = cv2.convertScaleAbs(robert_grad_x)
robert_grad_y = cv2.convertScaleAbs(robert_grad_y)
robert = cv2.addWeighted(src1=robert_grad_x, alpha=0.5, src2=robert_grad_y, beta=0.5, gamma=0)


# prewitt
prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)
prewitt_grad_x = cv2.filter2D(img, cv2.CV_16S, prewitt_x)
prewitt_grad_y = cv2.filter2D(img, cv2.CV_16S, prewitt_y)
prewitt_grad_x = cv2.convertScaleAbs(prewitt_grad_x)
prewitt_grad_y = cv2.convertScaleAbs(prewitt_grad_y)
prewitt = cv2.addWeighted(src1=prewitt_grad_x, alpha=0.5, src2=prewitt_grad_y, beta=0.5, gamma=0)


# Laplacian
lap = cv2.Laplacian(img, cv2.CV_64F)


cv2.imshow('Scharr', scharr)
cv2.imshow('robert', robert)
cv2.imshow('Prewitt', prewitt)
cv2.imshow('Lap', lap)

cv2.waitKey(0)
cv2.destroyAllWindows()



