import cv2
import numpy as np

# 图像的像素位操作(逻辑操作)

src1 = cv2.imread('LinuxLogo.jpg')
src2 = cv2.imread('WindowsLogo.jpg')
cv2.imshow('Linux-Windows', np.hstack(([src1,src2])))

# and
dst1 = cv2.bitwise_and(src2, src1)

# or
dst2 = cv2.bitwise_or(src2, src1)

# not
dst3 = cv2.bitwise_not(src2, src1)

# xor
dst4 = cv2.bitwise_xor(src2, src1)

cv2.imshow('and-or-not-xor', np.hstack(([dst1, dst2, dst3, dst4])))

cv2.waitKey(0)
cv2.destroyAllWindows()


