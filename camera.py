import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("cannot open the camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("can't receive frame")
        break
    cv.imshow("camera", frame)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
