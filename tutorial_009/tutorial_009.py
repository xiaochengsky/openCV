import cv2
import numpy as np

# 图像的边界填充

img = cv2.imread('opencv-logo.png')
cv2.imshow('image', img)
print(img.shape)                        # (739, 600, 3)


# 边界填充常量
const = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=100)

# 边界填充镜像 fedcba|abcdef|fedcba
reflect = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_REFLECT)

# 边界填充原图边界处的最后一个元素 aaaaaa|abcdef|ffffff
replicate = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_REPLICATE)

# 边界"对称"填充 cdefgh|abcdefgh|abcdef
wrap = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_WRAP)


cv2.imshow('const', const)
cv2.imshow('reflect', reflect)
cv2.imshow('replicate', replicate)
cv2.imshow('wrap', wrap)

cv2.waitKey(0)
cv2.destroyAllWindows()

