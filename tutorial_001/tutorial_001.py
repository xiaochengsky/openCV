import cv2

# 读取图片
# 显示图片及大小

img = cv2.imread('lena.jpg')
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
print(img.shape)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

