import cv2
from matplotlib import pyplot as plt


# 图像的双边滤波

img = cv2.imread("messi5.jpg")
cv2.imshow("input", img)

# params: 待处理图像, 9领域空间, 空间Gauss标准差, 灰度相似性Gauss函数标准差
bilater = cv2.bilateralFilter(img, 9, 100, 10)

# 可见图像内部的纹理被模糊, 但保留了边界
cv2.imwrite('messi5_bilater.jpg', bilater)
cv2.imshow("bilater", bilater)

cv2.waitKey(0)
cv2.destroyAllWindows()



