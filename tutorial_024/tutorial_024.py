import cv2
import random
import numpy as np
from matplotlib import pyplot as plt


# 图像添加高斯噪声和椒盐噪声

def sp_noise(image, prob):
    '''
    添加椒盐噪声
    prob:噪声比例
    '''
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


def gaussian_noise(image, mean=0, var=0.001):
    '''
        添加高斯噪声
        mean : 均值
        var : 方差
    '''
    image = np.array(image/255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out*255)
    return out


img = cv2.imread('sky.png')

sp = sp_noise(img, 0.02)
cv2.imwrite('sky_sp_noise.png', sp)
cv2.imshow('sp', sp)

gauss = gaussian_noise(img)
cv2.imwrite('sky_gauss_noise.png', gauss)
cv2.imshow('guass', gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()



