import cv2
import math
import osascript
import numpy as np
from HandTrackingModule import FindHands

cap = cv2.VideoCapture(1)
detector = FindHands()

minVol = 0
maxVol = 8

while True:
    succeed, img = cap.read()
    hand1_positions = detector.getPosition(img, range(21), draw=False)

    if len(hand1_positions) != 0:
        x1, y1 = hand1_positions[4][0], hand1_positions[4][1]
        x2, y2 = hand1_positions[8][0], hand1_positions[8][1]
        cv2.circle(img, hand1_positions[8], 5, (255,0,0), cv2.FILLED)
        cv2.circle(img, hand1_positions[4], 5, (255,0,0), cv2.FILLED)
        length1 = math.hypot(x2 - x1, y2 - y1)
        if length1 <35:
            volume = np.interp(x2, [600, 900], [maxVol, minVol])
            osascript.run('set Volume ' + str(volume))
            print (x2, volume)

    # cv2.imshow("Image", img)
    # if cv2.waitKey(1) == ord('q'):
    #     break
