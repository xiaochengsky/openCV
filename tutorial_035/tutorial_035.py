import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像的二值图像基本操作

img = cv2.imread('messi5.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('input', img)
cv2.imshow('gray', gray)


h, w = gray.shape
threshold = cv2.mean(gray)[0]
print("the img's threshold: ", threshold)

# 方式一
# binary = np.zeros([h, w], dtype=np.uint8)
# for row in range(h):
#     for col in range(w):
#         if gray[row, col] > threshold:
#             binary[row, col] = 255
#         else:
#             binary[row, col] = 0
# cv2.imshow('binary', binary)

# 方式二
# for i in range(5):
#     ret, binary = cv2.threshold(gray, threshold, 255, i)
#     cv2.imshow("binary_" + str(i), binary)

# 方式三
binary = np.zeros([h, w], dtype=np.uint8)
binary[np.where(gray > threshold)] = 255
cv2.imshow('binary', binary)

cv2.waitKey(0)
cv2.destroyAllWindows()



