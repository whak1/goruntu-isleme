import cv2 as cv
import numpy as np
img = cv.imread("baboon.bmp",0)
cv.imshow("duz",img)
cv.waitKey()
buyuk = np.max(img)
w,h=img.shape

for i in range(w):
    for j in range(h):
        img[i,j] = buyuk-img[i,j]

cv.imshow("ters",img)
cv.waitKey()
#dizi gösterimi
#print(img)