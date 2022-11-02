import cv2 as cv
import numpy as np
img = cv.imread("baboon.bmp",0)
w,h=img.shape
arr = np.zeros(256)

for i in range(w):
    for j in range(h):
        a=img[i,j]
        arr[a]=arr[a]+1

np.set_printoptions(suppress=True)
print(*arr)