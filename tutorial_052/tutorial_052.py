import cv2
import numpy as np
from matplotlib import pyplot as plt

# 图像的形态学——击中-击不中
# 即在 A 图中找到结构元素s1, 并输出 s1 所在 A 图上的原点
# 1. 使用模板 s1 腐蚀原图 A ===> 这个过程可以理解为在原始图像(A)中寻找和击中结构(s1)完全匹配的模块，匹配上了之后，保留匹配部分的中心元素，作为腐蚀结果的一个元素
# 2. 使用模板 s2(s1的补集)对 B(A的补集)进行腐蚀 ===> 即在原始图像(A)上找到击不中结构(s2)与原始图像没有交集的位置，这个位置的元素保留，作为腐蚀结果的一个元素
# 3. 对两个结果进行取交集 ===> 取前两者的交集就是击中-击不中的结果
# 用一个小的结构元素（击中结构）去射击原始图像，击中的元素保留；再用一个很大的结构元素（击不中，一般取一个环状结构）去射击原始图像，击不中原始图像的位置保留。满足击中元素能击中and击不中元素不能击中的位置的元素就是最终的形状结果



img = cv2.imread('test.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (11, 11), (-1, -1))
hit_miss = cv2.morphologyEx(binary, cv2.MORPH_HITMISS, kernel)

cv2.imwrite('hit_miss.png', hit_miss)
cv2.imshow('hit_miss', hit_miss)

cv2.waitKey(0)
cv2.destroyAllWindows()
