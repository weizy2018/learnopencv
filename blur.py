import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('pic2.png', cv.IMREAD_COLOR)
if img is None:
    print('image read error')
    exit()
# filter2D
kernel = np.ones((5,5),np.float32)/25
filter2d= cv.filter2D(img,-1,kernel)
# blur
blur = cv.blur(img, (5, 5))

# gaussian blur
gaussian = cv.GaussianBlur(img,(5,5),0)

# median blur
median = cv.medianBlur(img, 5)

plt.subplot(231), plt.imshow(img[:, :, [2, 1, 0]])
plt.xticks([]), plt.yticks([])
plt.title('original image') 

plt.subplot(232), plt.imshow(filter2d[:, :, [2, 1, 0]])
plt.xticks([]), plt.yticks([])
plt.title('filter2D')

plt.subplot(233), plt.imshow(blur[:, :, [2, 1, 0]])
plt.xticks([]), plt.yticks([])
plt.title('blur')

plt.subplot(234), plt.imshow(gaussian[:, :, [2, 1, 0]])
plt.xticks([]), plt.yticks([])
plt.title('gaussian blur')

plt.subplot(235), plt.imshow(median[:, :, [2, 1, 0]])
plt.xticks([]), plt.yticks([])
plt.title('median blur')

plt.show()








