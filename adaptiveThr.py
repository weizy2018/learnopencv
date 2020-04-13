import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('sudoku.png', cv.IMREAD_GRAYSCALE)
if img is None:
    print('cannot read image')
    exit()

'''
cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()
'''

img = cv.medianBlur(img,5)

ret, glbthresh = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
meanthresh = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
gaussianthresh = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

plt.subplot(221), plt.imshow(img, cmap='gray')
plt.title('original image')
plt.xticks([]), plt.yticks([])

plt.subplot(222), plt.imshow(glbthresh, cmap='gray')
plt.title('global threshold')
plt.xticks([]), plt.yticks([])

plt.subplot(223), plt.imshow(meanthresh, cmap='gray')
plt.title('mean threshold')
plt.xticks([]), plt.yticks([])


plt.subplot(224)
plt.imshow(gaussianthresh, cmap='gray')
plt.title('gaussian threshold')
plt.xticks([]), plt.yticks([])


plt.show()