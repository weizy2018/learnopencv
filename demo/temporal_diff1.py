import numpy as np 
import cv2 as cv 

capture = cv.VideoCapture('/home/weizy/Programs/opencv/opencv-4.1.0/samples/data/vtest.avi')
ret, frame1 = capture.read()

count = 0
while True:
    ret, frame2 = capture.read()
    if not ret:
        break 
    
    d_frame = cv.absdiff(frame2, frame1)
    cv.imshow("d_frame", d_frame)
    frame1 = frame2 

    key = cv.waitKey(30)
    if key == ord('q'):
        break
    
    if key == ord('s'):
        cv.imwrite("pic/temporal1.jpg", d_frame)
        print("count = ", count)
    
    count = count + 1

capture.release()
cv.destroyAllWindows()