import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像的 Laplacian 金字塔


def laplacian_demo(pyramid_images):
    level = len(pyramid_images)

    for i in range(level-1, -1, -1):
        if (i-1) < 0:
            h, w = img.shape[:2]
            expand = cv2.pyrUp(pyramid_images[i], dstsize=(w, h))
            lpls = cv2.subtract(img, expand) + 127
            cv2.imshow('laplacian' + str(i), lpls)
        else:
            h, w = pyramid_images[i-1].shape[:2]
            expand = cv2.pyrUp(pyramid_images[i], dstsize=(w, h))
            lpls = cv2.subtract(pyramid_images[i-1], expand) + 127
            cv2.imshow('laplacian' + str(i), lpls)


def pyramid_laplacian_down(image, level=3):
    temp = image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv2.pyrDown(temp)
        pyramid_images.append(dst)
        temp = dst.copy()
    return pyramid_images


img = cv2.imread('messi5.jpg')
cv2.imshow('input', img)
laplacian_demo(pyramid_laplacian_down(img))

cv2.waitKey(0)
cv2.destroyAllWindows()



