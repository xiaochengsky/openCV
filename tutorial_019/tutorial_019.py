import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像的直方图均衡化

# 将图像转换成一维数组, 再统计 [x, y, 3] ---> [x * y * 3]
def img_hist(image):
    plt.hist(image.ravel(), 256, [0, 256])
    plt.xlabel('Bins')
    plt.ylabel('Ranges')
    plt.show()


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


img = cv2.imread('messi5.jpg')
img_rgbhist(img)
img_hist(img)

cv2.waitKey(0)
cv2.destroyAllWindows()



