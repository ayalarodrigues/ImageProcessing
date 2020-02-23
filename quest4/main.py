import cv2

img_rgb = cv2.imread("arara.jpg", 1)
cv2.imshow("Image RGB", img_rgb)
img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)

cv2.imshow("Image HSV", img_hsv)
cv2.imwrite("Image_HSV.jpg", img_hsv)

h,s,v = cv2.split(img_rgb)

cv2.imshow("Channel H", h)
cv2.imwrite("Channel_H(Tonalidade).jpg", h)
cv2.imshow("Channel S", s)
cv2.imwrite("Channel_S(Saturação).jpg", s)
cv2.imshow("Channel V", v)
cv2.imwrite("Channel_V(Brilho).jpg", v)

cv2.waitKey(0)