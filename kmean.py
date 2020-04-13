import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(25, 100, 25)
y = np.random.randint(175, 255, 25)
z = np.hstack((x, y))
z = z.reshape((50, 1))
z = np.float32(z)

# plt.hist(z, 255, [0, 256])
# plt.show()

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
compactness, labels, centers = cv.kmeans(z, 2, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

A = z[labels == 0]
B = z[labels == 1]

print(centers)

plt.hist(A, 256, [0, 256], color='r')
plt.hist(B, 256, [0, 256], color='b')
plt.hist(centers, 32, [0, 256], color='y')
plt.show()
