import imutils
import cv2


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def sort_contours(cnts, method="left-to-right"):
    reverse = False
    i = 0
    if method == "right-to-left":
        reverse = True
        i = 1
    # 附上矩形边框, 获得矩形边框的 x, y, h, w
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    # key 从 lambda 表达式选择 boundingBoxes 作为排序对象, i 矩形的左上角点(i=0) 或右上角点(i=1)的选择
    cnts, boundingBoxes = zip(*sorted(zip(cnts, boundingBoxes), key=lambda x: x[1][i], reverse=reverse))

    return cnts, boundingBoxes


def resize(image, width=None, height=None, inter=cv2.INTER_NEAREST):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        ratio = height / float(h)
        dim = (int(w * ratio), height)
    else:
        ratio = width / float(w)
        dim = (width, int(h * ratio))
    resized = cv2.resize(image, dim, interpolation=inter)
    return resized
