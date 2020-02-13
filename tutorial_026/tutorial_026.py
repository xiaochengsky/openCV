import cv2
from matplotlib import pyplot as plt


# 图像的中值滤波

img = cv2.imread("sky_sp_noise.png")
cv2.imshow("input", img)

median = cv2.medianBlur(img, 5)
cv2.imwrite('sky_blur_sp_noise.png', median)
cv2.imshow("median ksize=5", median)

cv2.waitKey(0)
cv2.destroyAllWindows()



