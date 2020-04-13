import cv2 as cv
import numpy as np

lookUpTable = np.empty((1, 256), np.uint8)
for i in range(256):
    lookUpTable[0, i] = np.clip(i+5, 0, 255)

print(lookUpTable)
source = np.eye(5, dtype=np.uint8)
res = cv.LUT(source, lookUpTable)
print("source")
print(source)
print("res")
print(res)