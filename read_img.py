import cv2 as cv

img = cv.imread("/home/weizy/Pictures/2.png", cv.IMREAD_COLOR)

cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()
