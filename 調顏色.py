import cv2
import numpy as np
cv2.namedWindow("image_win")
def update(x):
        pass
params = []

#input picture
src = cv2.imread("input//201_446.png")
#change color base
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
#設定區間
cv2.createTrackbar('H_m','image_win',0,180,update)
cv2.createTrackbar('S_m','image_win',0,255,update)
cv2.createTrackbar('V_m','image_win',0,255,update)
cv2.createTrackbar('H_M','image_win',0,180,update)
cv2.createTrackbar('S_M','image_win',0,255,update)
cv2.createTrackbar('V_M','image_win',0,255,update)
while True: 
    if cv2.waitKey(10) & 0xFF == ord("q"):#按q離開
            break
    Hm = cv2.getTrackbarPos('H_m','image_win')
    Sm = cv2.getTrackbarPos('S_m', 'image_win')
    Vm = cv2.getTrackbarPos('V_m', 'image_win')
    HM = cv2.getTrackbarPos('H_M','image_win')
    SM = cv2.getTrackbarPos('S_M', 'image_win')
    VM = cv2.getTrackbarPos('V_M', 'image_win')

    #按內容做2值化
    Binary = cv2.inRange(hsv,(Hm,Sm,Vm),(HM,SM,VM))
    #show 結果
    cv2.imshow("Binary",Binary)
    
cv2.destroyAllWindows()