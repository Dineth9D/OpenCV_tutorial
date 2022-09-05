import cv2

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    sucess, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Lena", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


imgGray = cv2.cvtColor(img, cv2.COLOR_BayerGR2BGRA)
