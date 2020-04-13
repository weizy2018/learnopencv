import numpy as np 
import cv2 as cv 
import matplotlib.pyplot as plt 

img1 = cv.imread("pic/box.png", cv.IMREAD_GRAYSCALE)
img2 = cv.imread("pic/box_in_scene.png", cv.IMREAD_GRAYSCALE)

sift = cv.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

bf = cv.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)
print("type(matches): ", type(matches))
good = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good.append([m])

img3 = cv.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
plt.imshow(img3)
plt.show()



