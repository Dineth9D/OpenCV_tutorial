import cv2

path = "Resources/Building.jpg"
img = cv2.imread(path)
print(img.shape)

width, height = 400, 500
imgResize = cv2.resize(img, (height, width))
print(imgResize.shape)

imgCroped = img[300:540, 0:900]
print(imgCroped.shape)

cv2.imshow("road", img)
cv2.imshow("Bridge", imgResize)
cv2.imshow("Road Croped", imgCroped)


cv2.waitKey(0)
