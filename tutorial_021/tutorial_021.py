import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像的直方图比较
# img1 分别与 img2, img3 比较


# 统计 RGB 三通道的像素分布
def img_rgbhist(image):
    cv2.imshow('input', image)
    color = ['blue', 'green', 'red']
    for k, v in enumerate(color):
        # params: 图像, 通道, mask掩模, BINS(像素数), RANGE(像素范围)
        hist = cv2.calcHist([image], [k], None, [256], [0, 256])
        plt.plot(hist, color=v)
        plt.xlim([0, 256])
        plt.xlabel('Bins')
        plt.ylabel('Ranges')
    plt.show()


# 读取2副图, img1 == img2
img1 = cv2.imread('messi5.jpg')
img2 = np.copy(img1)
img3 = cv2.imread('opencv-logo.png')


# 转换到 hsv 空间
hsv1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
hsv3 = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)

# h s 通道                                  h:180 s:256       range
hist1 = cv2.calcHist([hsv1], [0, 1], None, [180, 256], [0, 180, 0, 256])
hist2 = cv2.calcHist([hsv2], [0, 1], None, [180, 256], [0, 180, 0, 256])
hist3 = cv2.calcHist([hsv3], [0, 1], None, [180, 256], [0, 180, 0, 256])

print(hist1.shape)

cv2.normalize(hist1, hist1, 0, 1.0, cv2.NORM_MINMAX)
cv2.normalize(hist2, hist2, 0, 1.0, cv2.NORM_MINMAX)
cv2.normalize(hist3, hist3, 0, 1.0, cv2.NORM_MINMAX)

#               相关性比较,            卡方比较             十字交叉性                巴氏距离
methods = [cv2.HISTCMP_CORREL, cv2.HISTCMP_CHISQR, cv2.HISTCMP_INTERSECT, cv2.HISTCMP_BHATTACHARYYA]

for method in methods:
    compare1_2 = cv2.compareHist(hist1, hist2, method)
    compare1_3 = cv2.compareHist(hist1, hist3, method)
    if method == cv2.HISTCMP_CORREL:
        comp_method = "Correlation"
    if method == cv2.HISTCMP_CHISQR:
        comp_method = "Chi-square"
    if method == cv2.HISTCMP_INTERSECT:
        comp_method = "Intersection"
    if method == cv2.HISTCMP_BHATTACHARYYA:
        comp_method = "Bhattacharyya"

    print("%s: compare1_2 = %.2f, compare1_3 = %.2f" % (comp_method, compare1_2, compare1_3))


# output
# Correlation: compare1_2 = 1.00, compare1_3 = 0.16
# Chi-square: compare1_2 = 0.00, compare1_3 = 64.34
# Intersection: compare1_2 = 59.42, compare1_3 = 0.56
# Bhattacharyya: compare1_2 = 0.00, compare1_3 = 0.95


