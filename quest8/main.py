import cv2

image = cv2.imread("paisagem.jpg", 1)
cv2.imshow("Original Image", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray)

rows, cols = gray.shape

red1 = cv2.resize(gray, (2*rows, 2*cols))

cv2.imshow("160x120", red1)
cv2.imwrite("160x120.jpg", red1)

red2 = cv2.resize(gray, (int(rows/2), int(cols/2)))

cv2.imshow("640x480", red2)
cv2.imwrite("640x480.jpg", red2)

cv2.waitKey(0)