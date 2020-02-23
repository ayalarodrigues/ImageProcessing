import cv2

img_rgb = cv2.imread("arara.jpg", 1)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Image", img_rgb)

cv2.imshow("Image Gray", img_gray)

cv2.imwrite("arara_Gray.jpg", img_gray)

cv2.waitKey(0)