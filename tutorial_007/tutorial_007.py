import cv2
import numpy as np

# 图像的混合操作

src1 = cv2.imread('LinuxLogo.jpg')
src2 = cv2.imread('WindowsLogo.jpg')
cv2.imshow('Linux-Windows', np.hstack(([src1, src2])))

# 偏置
gamma = 0

dst1 = cv2.addWeighted(src1, 0.9, src2, 0.1, gamma)
dst2 = cv2.addWeighted(src1, 0.5, src2, 0.5, gamma)
dst3 = cv2.addWeighted(src1, 0.1, src2, 0.9, gamma)

cv2.imshow('9:1---1:1---1:9', np.hstack(([dst1, dst2, dst3])))

cv2.waitKey(0)
cv2.destroyAllWindows()


