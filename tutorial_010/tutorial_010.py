import cv2
import numpy as np

# 图像的像素值统计

src = cv2.imread('opencv-logo.png')
cv2.imshow('src', src)


gray = cv2.imread('opencv-logo.png', cv2.IMREAD_GRAYSCALE)
print('img.shape: ', gray.shape)                        # (739, 600)

# 获取最小和最大像素点的值, 以及对应的位置
min, max, minLoc, maxLoc = cv2.minMaxLoc(gray)
print("min: %.2f, max: %.2f" % (min, max))
print("min loc: ", minLoc)
print("max loc: ", maxLoc)

# 获取图片像素的均值和方差
means, stddev = cv2.meanStdDev(gray)
print("mean: %.2f, stddev: %.2f" % (means, stddev))

# 使用均值对图片进行二值化
binary = np.copy(gray)
binary[np.where(binary < means)] = 0
binary[np.where(binary > means)] = 255

cv2.imshow('gray---binary', np.hstack([gray, binary]))

cv2.waitKey(0)
cv2.destroyAllWindows()

