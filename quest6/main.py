import cv2

image = cv2.imread("arara.jpg", 1)
cv2.imshow("Imagem", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagem Cinza", gray)

canny_img = cv2.Canny(gray, 80, 180)
cv2.imshow("Imagem Canny", canny_img)

cv2.waitKey()
cv2.imwrite("image_canny.jpg", canny_img)