import cv2
import numpy as np
from matplotlib import pyplot as plt

# 图像的二值化——寻找联通组件

img = cv2.imread('messi5.jpg')
h, w = img.shape[:2]


def connected_components_stats_demo(src):
    src = cv2.GaussianBlur(src, (3, 3), 0)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imshow("binary", binary)

    # return:
    # num_labels: 个数
    # labels: 当前寻找到的像素的第几个轮廓 ()
    # stats: 每个轮廓的中心坐标和宽高 (x,y,width,height)
    num_labels, labels, stats, centers = cv2.connectedComponentsWithStats(binary, connectivity=8, ltype=cv.CV_32S)
    print(num_labels)
    print(labels.shape)
    print(stats.shape)
    print(centers.shape)
    colors = []
    for i in range(num_labels):
        b = np.random.randint(0, 256)
        g = np.random.randint(0, 256)
        r = np.random.randint(0, 256)
        colors.append((b, g, r))

    colors[0] = (0, 0, 0)
    image = np.copy(src)
    for t in range(1, num_labels, 1):
        x, y, w, h, area = stats[t]
        cx, cy = centers[t]
        cv2.circle(image, (np.int32(cx), np.int32(cy)), 2, (0, 255, 0), 2, 8, 0)
        cv2.rectangle(image, (x, y), (x+w, y+h), colors[t], 1, 8, 0)
        cv2.putText(image, "num:" + str(t), (x, y), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255), 1);
        print("label index %d, area of the label : %d" % (t, area))

    cv2.imshow("colored labels", image)
    cv2.imwrite("./labels.png", image)
    print("total rice : ", num_labels - 1)


input = cv2.imread("opencv-logo.png")
connected_components_stats_demo(input)
cv2.waitKey(0)
cv2.destroyAllWindows()
