import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('/home/weizy/Pictures/zhao.png', cv.IMREAD_COLOR)
# b, g, r = cv.split(img)
# img2 = cv.merge([r, g, b])
img2 = img[:, :, [2, 1, 0]]

plt.subplot(121), plt.imshow(img)
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(img2)
plt.xticks([]), plt.yticks([])

plt.show()

# cv.namedWindow("img1", cv.WINDOW_NORMAL)
# cv.namedWindow('img2', cv.WINDOW_NORMAL)

# cv.imshow("img1", img)
# cv.imshow("img2", img2)
# cv.waitKey(0)
# cv.destroyAllWindows()
