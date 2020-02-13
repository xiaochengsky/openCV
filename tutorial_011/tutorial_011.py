import cv2
import numpy as np

# 图像的像素值归一化

src = cv2.imread("./opencv-logo.png")
cv2.imshow("input", src)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 转换为浮点数类型数组
gray = np.float32(gray)
print(gray.shape)

# scale and shift by NORM_MINMAX ---> gray[:, :] normalize to [alpha, beta]
norm_minmax = np.zeros(gray.shape, dtype=np.float32)
cv2.normalize(gray, dst=norm_minmax, alpha=0, beta=1.0, norm_type=cv2.NORM_MINMAX)
# print(norm_minmax)
cv2.imshow("NORM_MINMAX", np.uint8(norm_minmax*255))

# scale and shift by NORM_INF
norm_inf = np.zeros(gray.shape, dtype=np.float32)
cv2.normalize(gray, dst=norm_inf, alpha=1.0, beta=0, norm_type=cv2.NORM_INF)
# print(norm_inf)
cv2.imshow("NORM_INF", np.uint8(norm_inf*255))

# scale and shift by NORM_L1
norm_L1 = np.zeros(gray.shape, dtype=np.float32)
cv2.normalize(gray, dst=norm_L1, alpha=1.0, beta=0, norm_type=cv2.NORM_L1)
print(norm_L1)
cv2.imshow("NORM_L1", np.uint8(norm_L1*10000000))

# scale and shift by NORM_L2
norm_L2 = np.zeros(gray.shape, dtype=np.float32)
cv2.normalize(gray, dst=norm_L2, alpha=1.0, beta=0, norm_type=cv2.NORM_L2)
print(norm_L2)
cv2.imshow("NORM_L2", np.uint8(norm_L2*10000))

cv2.waitKey(0)
cv2.destroyAllWindows()

