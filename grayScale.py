import cv2

path = "Resources/lena.jpg"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Lena", img)
cv2.imshow("LenaGary", imgGray)
cv2.waitKey(0)
