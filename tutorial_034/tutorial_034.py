import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像的模板匹配

img = cv2.imread('opencv-logo.png')
target = cv2.imread('opencv-blue-logo.png')
cv2.imshow('input', img)
cv2.imshow('target', target)

methods = [cv2.TM_SQDIFF_NORMED, cv2.TM_CCORR_NORMED, cv2.TM_CCOEFF_NORMED]
th, tw = target.shape[:2]
for method in methods:
    result = cv2.matchTemplate(img, target, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 左上
    if method == cv2.TM_SQDIFF_NORMED:
        tl = min_loc
    else:
        tl = max_loc
    # 右下
    dr = (tl[0] + tw, tl[1] + th)
    cv2.rectangle(img, tl, dr, (0, 0, 255), 2)
    cv2.imshow('match' + np.str(method), img)

cv2.waitKey(0)
cv2.destroyAllWindows()



