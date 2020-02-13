import cv2
import numpy as np

# 图像的像素操作(加减乘除)

src1 = cv2.imread('LinuxLogo.jpg')
src2 = cv2.imread('WindowsLogo.jpg')
cv2.imshow('Linux-Windows', np.hstack(([src1,src2])))

# add
# 220 + 55 => 255
dst1 = cv2.add(src2, src1)

# sub
# 55 - 220 => 0
dst2 = cv2.subtract(src2, src1)

# mul
dst3 = cv2.multiply(src2, src1)

# div
dst4 = cv2.divide(src2, src1)

cv2.imshow('add-sub-mul-div', np.hstack(([dst1, dst2, dst3, dst4])))

cv2.waitKey(0)
cv2.destroyAllWindows()


