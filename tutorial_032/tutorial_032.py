import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像的 Gauss 金字塔


def pyramid_up(image, level=2):
    tmp = image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv2.pyrUp(tmp)
        pyramid_images.append(dst)
        cv2.imshow('pyramid_up' + str(i+1), dst)
        tmp = dst.copy()

    return pyramid_images


def pyramid_down(pyramid_images):
    level = len(pyramid_images)
    for i in range(level-1, -1, -1):
        dst = cv2.pyrDown(pyramid_images[i])
        cv2.imshow('pyramid_down' + str(i+1), dst)


img = cv2.imread('messi5.jpg')
cv2.imshow('input', img)
pyramid_down(pyramid_up(img))

cv2.waitKey(0)
cv2.destroyAllWindows()



