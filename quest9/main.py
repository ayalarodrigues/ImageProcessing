import cv2

image = cv2.imread('paisagem.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray Image', gray)
#cv2.waitKey(0)
rows, cols = gray.shape

with open('matriz.txt', 'w') as outfile:
    for row in range(rows):
        for col in range(cols):
            outfile.write(str(gray[row, col]) + ' ')
        outfile.write('\n')