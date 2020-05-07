import numpy as np 
import cv2 as cv 

capture = cv.VideoCapture('/home/weizy/Programs/opencv/opencv-4.1.0/samples/data/vtest.avi')
ret, frame1 = capture.read()
ret, frame2 = capture.read()

count = 0
while True:
    ret, frame3 = capture.read()
    if not ret:
        break 
    
    d_frame1 = cv.absdiff(frame2, frame1)
    d_frame2 = cv.absdiff(frame3, frame2)
    
    frame1 = frame2
    frame2 = frame3

    dst = cv.bitwise_and(d_frame1, d_frame2)
    cv.imshow("diff", dst)

    key = cv.waitKey(30)
    if key == ord('q'):
        break
    
    # if key == ord('s'):
    if count == 375:
        cv.imwrite("pic/temporal2.jpg", dst)
        print("count = ", count)
    
    count = count + 1

capture.release()
cv.destroyAllWindows()