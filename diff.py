import cv2 as cv
import numpy as np

cap = cv.VideoCapture('/home/weizy/Programs/opencv/opencv-4.1.0/samples/data/vtest.avi')
# cap = cv.VideoCapture(0)
if not cap.isOpened():
    print('can not the open camera')
    exit()

cv.namedWindow('source', cv.WINDOW_NORMAL)
cv.namedWindow('diff', cv.WINDOW_NORMAL)
cv.namedWindow("morphology", cv.WINDOW_NORMAL)

kernal = np.ones((9, 9), np.uint8)

while True:
    ret1, frame1 = cap.read()
    ret2, frame2 = cap.read()
    ret3, frame3 = cap.read()
    if not ret1 or not ret2 or not ret3:
        print('cannot receive frame')
        break
    cv.imshow('source', frame1)


    frame1 = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
    frame2 = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)
    frame3 = cv.cvtColor(frame3, cv.COLOR_BGR2GRAY)

    diff1 = cv.absdiff(frame1, frame2)
    diff2 = cv.absdiff(frame2, frame3)

    diff3 = cv.bitwise_and(diff1, diff2)

    ret, diff = cv.threshold(diff3, 30, 255.0, cv.THRESH_BINARY)
    

    # diff = cv.dilate(diff, None, iterations = 1)
    # diff = cv.erode(diff, None, iterations = 1)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    dst = cv.morphologyEx(diff, cv.MORPH_OPEN, kernel)

    cv.imshow("diff", diff)
    cv.imshow("morphology", dst)
    q = cv.waitKey(50)
    if q == ord('q'):
        break


cv.destroyAllWindows()


