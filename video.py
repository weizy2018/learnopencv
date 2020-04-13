import cv2 as cv

cap = cv.VideoCapture("/home/weizy/Videos/video.mp4")

if not cap.isOpened():
    exit()

ret, frame = cap.read()
cv.namedWindow('video', cv.WINDOW_NORMAL)

while ret:
    cv.imshow("video", frame)
    if cv.waitKey(1) == ord('q'):
        break
    ret, frame = cap.read()
    

cap.release()
cv.destroyAllWindows()
