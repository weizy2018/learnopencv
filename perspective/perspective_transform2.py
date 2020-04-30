import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

img1 = cv.imread("pic/box.png", cv.IMREAD_COLOR)
img2 = cv.imread("pic/box_in_scene.png", cv.IMREAD_COLOR)

img1_gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
img2_gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

surf = cv.xfeatures2d.SURF_create(400)

kp1, des1 = surf.detectAndCompute(img1_gray, None)
kp2, des2 = surf.detectAndCompute(img2_gray, None)

FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)
flann = cv.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1, des2, k = 2)
good = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good.append(m)

MIN_MATCH_COUNT = 10
if len(good) > MIN_MATCH_COUNT:
    # frame1_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    #     frame2_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    #     M, mask = cv.findHomography(frame1_pts, frame2_pts, cv.RANSAC, 5.0)
    img1_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    img2_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    M, mask = cv.findHomography(img1_pts, img2_pts, cv.RANSAC, 5.0)
    rows, cols, ch = img2.shape
    warp = cv.warpPerspective(img1, M, (cols, rows))

    sub = cv.absdiff(img2, warp)

    plt.subplot(221), plt.title("img1")
    plt.imshow(img1[:, :, [2, 1, 0]])

    plt.subplot(222), plt.title("img2")
    plt.imshow(img2[:, :, [2, 1, 0]])

    plt.subplot(223), plt.title("absdiff")
    plt.imshow(sub[:, :, [2, 1, 0]])

    plt.subplot(224), plt.title("warp")
    plt.imshow(warp[:, :, [2, 1, 0]])
    plt.show()



