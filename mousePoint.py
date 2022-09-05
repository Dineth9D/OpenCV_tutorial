import cv2
import numpy as np


def mousePoints(event, x, y, flags, programs):
    if(event == cv2.EVENT_LBUTTONDOWN):
        print(x, y)


img = cv2.imread('Resources/cards.jpg')
cv2.imshow('Original Image', img)
cv2.setMouseCallback("Original Image", mousePoints)

cv2.waitKey(0)
