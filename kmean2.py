import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(25, 50, (25, 2))
y = np.random.randint(60, 85, (25, 2))
z = np.vstack((x, y))
z = np.float32(z)
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret, labels, center = cv.kmeans(z, 2, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

A = z[labels.ravel() == 0]
B = z[labels.ravel() == 1]

plt.scatter(A[:, 0], A[:, 1])
plt.scatter(B[:, 0], B[:, 1], c = 'r')
plt.scatter(center[:, 0], center[:, 1], s = 80, c = 'y', marker='s')
plt.xlabel('Height'), plt.ylabel('Weight')
plt.show()
