import cv2
import numpy as np

img = cv2.imread("Resources/visitCard.jpg")

width, height = 350, 230
pts1 = np.float32([[229, 256], [550, 507], [34, 411], [334, 719]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))


for x in range(0, 4):  # 0 to 4(but not including 4)
    cv2.circle(img, (int(pts1[x][0]), int(pts1[x][1])),
               5, (0, 0, 255), cv2.FILLED)


# cv2.circle(img, (231, 255), 5, (0, 0, 255), cv2.FILLED)
# cv2.circle(img, (429, 216), 5, (0, 0, 255), cv2.FILLED)
# cv2.circle(img, (281, 544), 5, (0, 0, 255), cv2.FILLED)
# cv2.circle(img, (500, 496), 5, (0, 0, 255), cv2.FILLED)

cv2.imshow("Original Image", img)
cv2.imshow("Output Image", imgOutput)
cv2.waitKey(0)
