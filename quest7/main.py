import cv2

image_rgb = cv2.imread("arara.jpg", 1)
cv2.imshow("RGB Image", image_rgb)

gray = cv2.cvtColor(image_rgb,  cv2.COLOR_RGB2GRAY)
cv2.imshow("Image Gray", gray)

ret, threshold_img = cv2.threshold(gray, 100, 200, cv2.THRESH_BINARY)
cv2.imshow("Image Thresholded", threshold_img)

cv2.waitKey(0)
cv2.imwrite("Image_Thresholded.jpg", threshold_img)