import cv2

# 将图片保存为灰度图(gray.jpg)
# 并保存

img = cv2.imread('lena.jpg')
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
print('image.shape: ', img.shape)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray.jpg', gray)
cv2.imread('gray.jpg', cv2.WINDOW_NORMAL)
cv2.imshow('gray', gray)
print('gray.shape: ', gray.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()

