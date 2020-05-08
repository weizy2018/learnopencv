import cv2 as cv 
import numpy as np 

def getThreshold(img):
    hist,bins = np.histogram(img.ravel(),256,[0,256])

    img_temp = img.ravel()
    minval = img_temp[0]
    maxval = img_temp[0]

    for i in range(len(img_temp)):
        if minval > img_temp[i]:
            minval = img_temp[i]
        if maxval < img_temp[i]:
            maxval = img_temp[i]

    print("type(minval): ", type(minval))

    threshold = 0
    newThreshold = (int)((minval + maxval) / 2)
    while newThreshold != threshold:
        sum1 = sum2 = 0
        w1 = w2 = 0
        print(type(minval))
        print("newThreshold: ", type(newThreshold))
        for i in range(minval, newThreshold):
            sum1 = sum1 + hist[i] * i
            w1 = w1 + hist[i]
        
        avg1 = sum1 / w1

        for i in range(newThreshold, maxval):
            sum2 = sum2 + hist[i] * i
            w2 = w2 + hist[i]
        
        avg2 = sum2 / w2

        threshold = newThreshold
        newThreshold = (int)((avg1 + avg2) / 2)

    return newThreshold


img = cv.imread("pic/sudoku.png", cv.IMREAD_GRAYSCALE)

thre = getThreshold(img)
print(thre)

ret, dst = cv.threshold(img, thre, 255, cv.THRESH_BINARY)
cv.imshow("dst", dst)
cv.waitKey(0)
cv.destroyAllWindows()