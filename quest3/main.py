import cv2

image_rgb = cv2.imread("arara.jpg", 1)

cv2.imshow("Original Image", image_rgb)

channel=[3]
r,g,b = cv2.split(image_rgb)

#cv2.namedWindow("Channel Red", 1)
cv2.imshow("Channel Red", r)
cv2.imwrite("Channel_Red.jpg", r)

#namedWindow("Channel Green", 1)
cv2.imshow("Channel Green", g)
cv2.imwrite("Channel_Green.jpg", g)

#namedWindow("Channel Blue", 1)
cv2.imshow("Channel Blue", b)
cv2.imwrite("Channel_Blue.jpg", b)

cv2.waitKey(0)