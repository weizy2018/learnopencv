import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('pic/pic1.jpg', cv.IMREAD_COLOR)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
corners = cv.goodFeaturesToTrack(gray, 25, 0.01, 10)
corners = np.int0(corners)
for i in corners:
    x, y = i.ravel()
    cv.circle(img, (x, y), 10, (0, 0, 255), -1)
img = img[:, :, [2, 1, 0]]
plt.imshow(img)
plt.show()
# cv.namedWindow('img', cv.WINDOW_NORMAL)
# cv.imshow('img', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

