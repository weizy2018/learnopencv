import numpy as np
import cv2 as cv

img = cv.imread('/home/weizy/Programs/opencv/opencv-4.1.0/samples/data/digits.png', cv.IMREAD_COLOR)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
x = np.array(cells)
print(x.shape)

train = x[:, :50].reshape(-1, 400).astype(np.float32)
test = x[:, 50:100].reshape(-1, 400).astype(np.float32)
print(train.shape)
print(test.shape)

k = np.arange(10)
train_labels = np.repeat(k, 250)[:, np.newaxis]
test_labels = train_labels.copy()
knn = cv.ml.KNearest_create()
knn.train(train, cv.ml.ROW_SAMPLE, train_labels)
ret, result, neighbours, dist = knn.findNearest(test, k = 5)

matches = result == test_labels
correct = np.count_nonzero(matches)
accuracy = correct*100.0 / result.size
print(accuracy)

