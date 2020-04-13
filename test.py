import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('sudoku.png', cv.IMREAD_GRAYSCALE)
if img is None:
    print('can not read img')
    exit()

img2 = cv.medianBlur(img, 5)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('original image')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(img2, cmap='gray')
plt.title('median blur')
plt.xticks([]), plt.yticks([])

plt.show()

