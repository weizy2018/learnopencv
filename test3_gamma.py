import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt 
images = ["pic/lena.jpg", "pic/pic1.jpg", "pic/pic2.jpg", "pic/Picture1.png", "pic/xianlu.jpg"]

gamma = 0.8
lookUpTable = np.empty((1, 256), np.uint8)
for i in range(256):
    lookUpTable[0, i] = np.clip(pow(i / 255, gamma) * 255, 0, 255)

for item in images:
    image = cv.imread(item, cv.IMREAD_COLOR)
    plt.subplot(221)
    plt.imshow(image[:, :, [2, 1, 0]])
    plt.xticks([]), plt.yticks([])
    plt.subplot(222)
    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    plt.hist(image_gray.ravel(), 256, [0, 256])
    
    image2 = cv.LUT(image, lookUpTable)
    plt.subplot(223)
    plt.imshow(image2[:, :, [2, 1, 0]])
    plt.xticks([]), plt.yticks([])
    plt.subplot(224)
    image2_gray = cv.cvtColor(image2, cv.COLOR_BGR2GRAY)
    plt.hist(image2_gray.ravel(), 256, [0, 256])

    plt.show()

    