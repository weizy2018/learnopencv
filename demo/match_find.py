import cv2 as cv 
import numpy as np 


sift = cv.xfeatures2d.SIFT_create()
FLANN_INDEX_KDTREE = 1
MIN_MATCH_COUNT = 10
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)
flann = cv.FlannBasedMatcher(index_params, search_params)

cv.namedWindow("match", cv.WINDOW_NORMAL)
cv.namedWindow("frame1", cv.WINDOW_NORMAL)
cv.namedWindow("frame2", cv.WINDOW_NORMAL)

path = "/home/weizy/files/毕设/毕业设计-于孟渤/于孟渤-代码/"
videoPath = path + "test.mp4"

capture = cv.VideoCapture('/home/weizy/Programs/opencv/opencv-4.1.0/samples/data/vtest.avi')
# capture = cv.VideoCapture(videoPath)
if not capture.isOpened():
    print("can not open the video")
    exit()

ret, frame2 = capture.read()
kp2, des2 = sift.detectAndCompute(frame2, None)
while True:
    frame1 = frame2
    kp1 = kp2
    des1 = des2

    ret, frame2 = capture.read()
    if not ret:
        break
    
    frame1_gray = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
    frame2_gray = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)

    # kp1, des1 = sift.detectAndCompute(frame1, None)
    kp2, des2 = sift.detectAndCompute(frame2, None)

    matches = flann.knnMatch(des1, des2, k = 2)
    good = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good.append(m)
    if len(good) > MIN_MATCH_COUNT:
        frame1_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        frame2_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        M, mask = cv.findHomography(frame1_pts, frame2_pts, cv.RANSAC, 5.0)
        matches_mask = mask.ravel().tolist()
        h, w, d = frame1.shape
        warp = cv.warpPerspective(frame1, M, (w, h))
        print("frame2: ", frame2.shape)
        print("warp: ", warp.shape)
        sub = cv.absdiff(frame2, warp)
        cv.imshow("sub", sub)
        '''
        pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
        dst = cv.perspectiveTransform(pts, M)
        frame2_poly = frame2.copy()
        frame2_poly = cv.polylines(frame2_poly, [np.int32(dst)], True, (0, 0, 255), 3, cv.LINE_AA)
        '''
    else:
        print("not enough matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT))
        matches_mask = None
    
    # img3 = cv.drawMatches(img1, kp1, img2, kp2, good, None, **draw_params)
    draw_params = dict(matchColor = (0, 255, 0),
                    singlePointColor = None,
                    matchesMask = matches_mask,
                    flags = 2)
    img = cv.drawMatches(frame1, kp1, frame2, kp2, good, None, **draw_params)

    cv.imshow("match", img)
    cv.imshow("frame1", frame1)
    cv.imshow("frame2", frame2)

    frame1 = frame2
    key = cv.waitKey(30)
    if key == ord('q'):
        break
    if key == ord('s'):
        cv.imwrite("pic/absdiff.jpg", sub)
    
capture.release()
cv.destroyAllWindows()



