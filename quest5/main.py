import cv2

image_rgb = cv2.imread("arara.jpg", 1)
image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image RGB", image_rgb)
cv2.imshow("Image Gray", image_gray)

img_median = cv2.medianBlur(image_gray, ksize=5)

cv2.imshow("Image Median", img_median)
cv2.imwrite("arara_median.jpg", img_median)

img_blur = cv2.blur(image_gray, ksize=(5, 5))
cv2.imshow("Image Blur", img_blur)
cv2.imwrite("arara_blur.jpg", img_blur)

cv2.waitKey(0)