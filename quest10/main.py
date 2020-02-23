import cv2
import numpy as np

image = cv2.imread('paisagem.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray Image', gray)
cv2.waitKey(0)

rows, cols = gray.shape[:2]

limi_matrix = np.zeros((rows, cols), dtype=np.uint8) #matriz de zeros

for row in range(rows):
    for col in range(cols):
        limi_matrix[row, col] = gray[row, col]

with open('matrix.txt', 'w') as outfile:
    for row in range(rows):
        for col in range(cols):

            if limi_matrix[row, col] < 100:
                limi_matrix[row, col] = 0
            else:
                limi_matrix[row, col] = 255

            outfile.write(str(limi_matrix[row, col]) + ' ')
        outfile.write('\n')