import cv2

img_rgb = cv2.imread("/Users/rodri/PycharmProjects/quest1/arara.jpg", 1)

cv2.imshow("Arara", img_rgb)

cv2.imwrite("/Users/rodri/PycharmProjects/quest1/Image.jpg", img_rgb)

cv2.waitKey(0)