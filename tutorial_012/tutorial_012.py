import cv2
import numpy as np

# 图像的伸缩与插值

img = cv2.imread("messi5.jpg")
cv2.namedWindow('input', cv2.WINDOW_NORMAL)
cv2.imshow("input", img)

# dst 可以为 None, 因为已知了 x, y 方向的缩放比
res_cubic1 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# dst 指定了 size, 则不需要 fx, fy
h, w = img.shape[:2]
res_cubic = cv2.resize(img, (2*w, 2*h), interpolation=cv2.INTER_CUBIC)

res_near = cv2.resize(img, (2*w, 2*h), interpolation=cv2.INTER_NEAREST)

res_linear = cv2.resize(img, (2*w, 2*h), interpolation=cv2.INTER_LINEAR)

res_lancz = cv2.resize(img, (2*w, 2*h), interpolation=cv2.INTER_LANCZOS4)

cv2.imshow('res_cubic---res_near---res_linear---res_lancz', np.hstack([res_cubic, res_near, res_linear, res_lancz]))

cv2.waitKey(0)
cv2.destroyAllWindows()

