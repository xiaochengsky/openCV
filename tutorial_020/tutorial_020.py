import cv2
from matplotlib import pyplot as plt


# 图像直方图均衡化以及自适应均衡化

# 将图像转换成一维数组, 再统计 [x, y, 3] ---> [x * y * 3]
def img_hist(image):
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show()


# 统计灰度图的像素分布
def img_grayhist(image):
    cv2.imshow('input', img)
    color = ['gray']
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.plot(hist, color='gray')
    plt.xlim([0, 256])
    plt.show()


img = cv2.imread('messi5.jpg', cv2.IMREAD_GRAYSCALE)

# 直方图均衡化
dst = cv2.equalizeHist(img)

# 自适应均衡化
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
adp = clahe.apply(img)

img_grayhist(img)
img_grayhist(dst)
img_grayhist(adp)

img_hist(img)
img_hist(dst)
img_hist(adp)

cv2.waitKey(0)
cv2.destroyAllWindows()



