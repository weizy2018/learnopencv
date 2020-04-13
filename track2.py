import cv2 as cv
import numpy as np

capture = cv.VideoCapture('/home/weizy/Programs/opencv/opencv-4.1.0/samples/data/vtest.avi')
ret, frame = capture.read()
prvs = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame)
hsv[..., 1] = 255

cv.namedWindow('sorce', cv.WINDOW_NORMAL)
cv.namedWindow('frame', cv.WINDOW_NORMAL)
while(1):
    ret, frame2 = capture.read()
    if not ret:
        break
    next = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)
    flow = cv.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    mag, ang = cv.cartToPolar(flow[..., 0], flow[..., 1])
    hsv[..., 0] = ang * 180 / np.pi / 2
    hsv[..., 2] = cv.normalize(mag, None, 0, 255, cv.NORM_MINMAX)
    bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
    cv.imshow('sorce', frame2)
    cv.imshow('frame', bgr)
    k = cv.waitKey(30)
    if k == ord('q'):
        break
    prvs = next


cv.destroyAllWindows()

