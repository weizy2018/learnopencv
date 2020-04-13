import cv2 as cv
import numpy as np

data = np.loadtxt('/home/weizy/Programs/opencv/opencv-4.1.0/samples/data/letter-recognition.data',
                    dtype='float32', delimiter=',', converters={0: lambda ch:ord(ch) - ord('A')})
train, test = np.vsplit(data, 2)
responses, trainData = np.hsplit(train, [1])
labels, testData = np.hsplit(test, [1])

knn = cv.ml.KNearest_create()
knn.train(trainData, cv.ml.ROW_SAMPLE, responses)
ret, result, neighbours, dist = knn.findNearest(testData, k = 5)
correct = np.count_nonzero(result == labels)
accuracy = correct*100.0 / 10000
print(accuracy)
