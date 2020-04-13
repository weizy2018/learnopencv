import cv2 as cv

def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    # cv.imshow("source", frame)
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x, y, w, h) in faces:
        center = (x + w // 2, y + h // 2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h, x:x+w]
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2, y2, w2, h2) in eyes:
            eye_center = (x + x2 + w2 // 2, y + y2 + h2 // 2)
            radius = int(round((w2 + h2) * 0.25))
            frame = cv.circle(frame, eye_center, radius, (255, 0, 0), 4)
    cv.imshow("face detection", frame)

cv.namedWindow("face detection", cv.WINDOW_NORMAL)
face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()
path = "/home/weizy/Programs/opencv/opencv-4.1.0/data/haarcascades_cuda/"
if not face_cascade.load(path + "haarcascade_frontalface_alt.xml"):
    print('face cascade file not found')
    exit(0)
if not eyes_cascade.load(path + "haarcascade_eye_tree_eyeglasses.xml"):
    print('eye cascade file not found')
    exit(0)

cap = cv.VideoCapture(0)
if not cap.isOpened:
    print("cannot open cammera")
    exit(0)
while True:
    ret, frame = cap.read()
    if not ret:
        print("frame error")
        break
    detectAndDisplay(frame)
    if cv.waitKey(10) == ord('q'):
        break

cv.destroyAllWindows()

