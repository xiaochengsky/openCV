import cv2
import argparse
import numpy as np
import utils

parse = argparse.ArgumentParser(
    description='IDcard classify')

parse.add_argument("-t", "--template", default='./images/template/tpl.png', required=False,
                   help="path to template OCR-A image")
parse.add_argument("-i", "--test", default='./images/test/credit_card_01.png', required=False,
                   help="path to input test image")
args = parse.parse_args()

# step1: 预处理模板图像
# 显示模板图像
tpl = cv2.imread(args.template)
cv2.imshow('tpl', tpl)

# 模板图像灰度图与二值化处理
gray = cv2.cvtColor(tpl, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
# 白底黑字所以用 THRESH_BINARY_INV, 而不是 THRESH_BINARY
threshold, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
print(threshold)
cv2.imshow('binary', binary)

# 获取模板图像的外轮廓, 保留终点坐标
ref, refCnts, hierarchy = cv2.findContours(binary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('ref', ref)
# 画出边框
cv2.drawContours(tpl, refCnts, -1, (0, 0, 255), 3)
cv2.imshow('tpl_Contours', tpl)
# print(np.array(refCnts))            # 10.


# 对模板图像进行排序, 方便从0-9对应存储
refCnts = utils.sort_contours(refCnts, method="left-to-right")[0]
digits = {}

# 遍历模板图形的每一个轮廓
for (k, v) in enumerate(refCnts):
    x, y, w, h = cv2.boundingRect(v)
    roi = ref[y: y + h, x: x + w]
    roi = cv2.resize(roi, (57, 88))
    # 按 method 方法进行存储, 每个数字代表一个模板
    digits[k] = roi

# step2: 预处理测试集图像
# 根据卡上字体大小, 初始化卷积核
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))
sqKerbel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# 读取测试图像
img = cv2.imread(args.test)
cv2.imshow('test_set', img)
img = utils.resize(img, width=300)
gray_t = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray_t', gray_t)

# 顶帽操作, 突出更明亮的区域
topHat = cv2.morphologyEx(gray_t, cv2.MORPH_TOPHAT, rectKernel)
cv2.imshow('topHat', topHat)

# 沿着 x 方向计算梯度
grad_x = cv2.Sobel(topHat, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=-1)
grad_x = np.absolute(grad_x)
(minVal, maxVal) = (np.min(grad_x), np.max(grad_x))
# 归一化处理 类似于 NORM_MINMAX 方式
grad_x = (255 * ((grad_x - minVal) / (maxVal - minVal)))
grad_x = grad_x.astype("uint8")

# print(np.array(grad_x).shape)
cv2.imshow('grad_x', grad_x)

# 通过闭操作, 将卡上靠近的数字连在一起
close_grad_x = cv2.morphologyEx(grad_x, cv2.MORPH_CLOSE, rectKernel)
cv2.imshow('close_grad_x', close_grad_x)

# 适合双峰二值化
thresh = cv2.threshold(close_grad_x, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imshow('thresh', thresh)

# 再做一个闭操作, 使得轮廓内的数字区更饱和
thresh_2 = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, sqKerbel)
cv2.imshow('thresh_2', thresh_2)

# 计算轮廓
thresh_, threshCnts, hierarchy = cv2.findContours(thresh_2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = threshCnts
cur_img = img.copy()
cv2.drawContours(cur_img, cnts, -1, (0, 0, 255), 3)
cv2.imshow('img', cur_img)
locs = []

# 遍历轮廓
for (k, v) in enumerate(cnts):
    # 计算矩形
    x, y, w, h = cv2.boundingRect(v)
    ar = w / float(h)

    # 选择合适的区域, 四个数字一组,
    if 2.5 < ar < 4.0:
        if (40 < w < 55) and (10 < h < 20):
            locs.append((x, y, w, h))

# 将符合的轮廓从左到右排序
locs = sorted(locs, key=lambda x: x[0])
output = []

# 遍历每一个轮廓中的数字
for i, (gX, gY, gW, gH) in enumerate(locs):
    groupOutput = []

    # 根据坐标提取每个数据区的轮廓组
    group = gray_t[gY - 5: gY + gH + 5, gX - 5: gX + gW + 5]
    group = cv2.threshold(group, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # 计算每个轮廓组中的4个数字的轮廓
    group_, digitCnts, hierarchy = cv2.findContours(group.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    digitCnts = utils.sort_contours(digitCnts, method="left-to--right")[0]

    for i in digitCnts:
        (x, y, w, h) = cv2.boundingRect(i)
        roi = group[y: y + h, x: x + w]
        roi = cv2.resize(roi, (57, 88))

        # 为每个数组匹配得分
        scores = []

        for (digit, digitROI) in digits.items():
            # 模板匹配
            result = cv2.matchTemplate(roi, digitROI, cv2.TM_CCOEFF)
            _, score, _, _ = cv2.minMaxLoc(result)
            scores.append(score)

        # 取分数最高的
        groupOutput.append(str(np.argmax(scores)))

    # 在图上标记
    cv2.rectangle(img, (gX - 5, gY - 5), (gX + gW + 5, gY + gH + 5), (0, 0, 255), 1)
    cv2.putText(img, "".join(groupOutput), (gX, gY - 15), cv2.FONT_HERSHEY_SIMPLEX, .7, (0, 0, 255), 2)

    # 得到结果
    output.extend(groupOutput)

# 输出结果
print("Credit Card Numbers#: {}".format("".join(output)))
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
