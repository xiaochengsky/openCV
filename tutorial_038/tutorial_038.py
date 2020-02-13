import cv2
import numpy as np
from matplotlib import pyplot as plt

# 图像的 Triangle 二值化

img = cv2.imread('messi5.jpg')
h, w = img.shape[:2]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('input', img)
cv2.imshow('gray', gray)

ret_triangle, binary_triangle = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
print("ret :", ret_triangle)
cv2.imshow("binary", binary_triangle)


cv2.waitKey(0)
cv2.destroyAllWindows()
