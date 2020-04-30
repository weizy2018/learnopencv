import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

img = cv.imread("pic/sudoku.png")
rows, cols, ch = img.shape

pts1 = np.float32([[76, 90], [492, 72], [39, 512], [519, 517]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
M = cv.getPerspectiveTransform(pts1, pts2)
dst = cv.warpPerspective(img, M, (300, 300))
plt.subplot(121)
plt.imshow(img), plt.title("Input")

plt.subplot(122)
plt.imshow(dst), plt.title("Output")
plt.show()