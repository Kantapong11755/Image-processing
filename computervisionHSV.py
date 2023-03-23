import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow('windows')
cv2.resizeWindow(winname='windows',width=300,height=350)

cv2.createTrackbar('HMin', 'windows', 0, 179, nothing)
cv2.createTrackbar('SMin', 'windows', 0, 255, nothing)
cv2.createTrackbar('VMin', 'windows', 0, 255, nothing)
cv2.createTrackbar('HMax', 'windows', 0, 179, nothing)
cv2.createTrackbar('SMax', 'windows', 0, 255, nothing)
cv2.createTrackbar('VMax', 'windows', 0, 255, nothing)

cv2.setTrackbarPos('HMax', 'windows', 179)
cv2.setTrackbarPos('SMax', 'windows', 255)
cv2.setTrackbarPos('VMax', 'windows', 255)

hMin = sMin = vMin = hMax = sMax = vMax = 0
phMin = psMin = pvMin = phMax = psMax = pvMax = 0

while(1):
    hMin = cv2.getTrackbarPos('HMin', 'windows')
    sMin = cv2.getTrackbarPos('SMin', 'windows')
    vMin = cv2.getTrackbarPos('VMin', 'windows')
    hMax = cv2.getTrackbarPos('HMax', 'windows')
    sMax = cv2.getTrackbarPos('SMax', 'windows')
    vMax = cv2.getTrackbarPos('VMax', 'windows')

    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])
    ret,frame = cap.read()
    
    hsv1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv1, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    if((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
        print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
        phMin = hMin
        psMin = sMin
        pvMin = vMin
        phMax = hMax
        psMax = sMax
        pvMax = vMax
        
    
    cv2.imshow('windows', result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
cap.release()
