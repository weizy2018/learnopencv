import numpy as np 
import cv2 as cv 
import matplotlib.pyplot as plt 

image = cv.imread("pic/lena.jpg", cv.IMREAD_GRAYSCALE)
plt.subplot(121)
plt.imshow(image, cmap='gray')
plt.subplot(122)
plt.hist(image.ravel(), 256, [0, 256])
plt.show()
