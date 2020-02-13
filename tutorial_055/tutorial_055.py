import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像的视频读写与处理

def video_process(img, opt=1):
    dst = None
    if opt == 0:
        dst = cv2.bitwise_not(img)
    if opt == 1:
        dst = cv2.GaussianBlur(img, (0, 0), 15)
    if opt == 2:
        dst = cv2.Canny(img, 100, 200)
    return dst


cap = cv2.VideoCapture(0)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)
print("height = %d, width = %d, count = %d, fps = %d" % (h, w, count, fps))
index = 0

while True:
    ret, frame = cap.read()
    if ret is True:
        cv2.imshow('video-input', frame)
        # 根据输入切换处理模式
        c = cv2.waitKey(50)
        if 49 <= c <= 51:
            index = c - 49

        result = video_process(frame, index)
        cv2.imshow('result', result)
        print('push %d' % index)

        # 按下 ESC
        if c == 27:
            break
    else:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()

