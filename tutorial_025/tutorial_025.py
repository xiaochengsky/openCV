import cv2
from matplotlib import pyplot as plt


# 图像的高斯滤波处理
# 高斯滤波: 作为低通滤波器除去高斯噪声

img = cv2.imread("sky_gauss_noise.png")
cv2.imshow("input", img)

# kernel = 5*5 的均值处理
dst1 = cv2.blur(img, (5, 5))

# 高斯模糊
# params: 处理图像, 高斯核大小(奇数), 沿 x,y 方向的标准差
dst2 = cv2.GaussianBlur(img, (5, 5), sigmaX=0)
dst3 = cv2.GaussianBlur(img, (5, 5), sigmaX=15)

cv2.imshow("blur ksize=5", dst1)
cv2.imshow("gaussian ksize=5", dst2)
cv2.imshow("gaussian sigmaX=15", dst3)

cv2.imwrite('sky_blur_gauss_noise.png', dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()



