import cv2
import cvzone
import numpy as np
import math
from trackbar import *
import serial


def Lockon():
    cv2.putText(frame, "nesne hedef bolgede", (5, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, RED, 2)


RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#port = serial.Serial("com4", 9600)  #Arduino kartının bağlı olduğu USB portu

cap = cv2.VideoCapture(0)
cap_width, cap_height = cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
scale = 1.5

width, height = int(cap_width*scale), int(cap_height*scale)
ccx, ccy = width//2, height//2  #pencerenin merkezi (ccx = cap center x, ccy = cap center y)
cr = math.sqrt((width/2)**2 + (height/2)**2)    #pencerenin merkezinin en yakın köşesine olan uzaklığı (cr = cap radius)

center_area = np.array([[ccx-50, ccy+50], [ccx-50, ccy-50], [ccx+50, ccy-50], [ccx+50, ccy+50]], dtype=np.int32)

hsv_prepare(title="mask")

while True:

    if cv2.waitKey(1) & 0xff == ord("q"):
        break

    scs, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (width, height))


    mask = hsv_finder("mask", frame)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    distance = None #nesnenin merkeze uzaklığı
    bboxct = 0  #bbox sayacı
    data = "0" #Arduino'ya gönderilecek veri, arama algoritmasını temsil ediyor

    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 2000:
                bboxct += 1
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x+w, y+h), BLUE, 2)   #nesnenin dikdörtgen ile belirtilmesi

                ocx, ocy = x+w//2, y+h//2  #boundingBox'ın merkezinin koordinatları (ocx=object center x, ocy = object center y)
                areaTest = cv2.pointPolygonTest(center_area, (ocx, ocy), False)   #merkez bölgesinde cismin olup olmamasının kontrolü
                cv2.circle(frame, (ocx, ocy), 3, BLUE, -1)
                cv2.line(frame, (ccx, ccy), (ocx, ocy), BLACK, 2)

                distance = int(math.sqrt((ocx-ccx)**2+(ocy-ccy)**2))  #nesnenin merkeze uzaklığı

                if areaTest > 0 and bboxct == 1:    #merkez bölgesi kontrol
                    data = "1"
                    Lockon()    #nesneye kilitlenme algoritması

                else:
                    if ocx > ccx and ocy < ccy:  #1. bölge kontrol
                        data = "2"
                    elif ocx < ccx and ocy < ccy:  #2. bölge kontrol
                        data = "3"
                    elif ocx < ccx and ocy > ccy:  #3. bölge kontrol
                        data = "4"
                    elif ocx > ccx and ocy > ccy:  #4. bölge kontrol
                        data = "5"



    if bboxct == 1:
        cv2.putText(frame, str(distance), (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, WHITE, 2)
    elif bboxct > 1:
        cv2.putText(frame, "birden fazla nesne tespit ediliyor", (5, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, RED, 2)


    cv2.line(frame, (0, height//2), (width, height//2), WHITE, 1) #yatay eksen
    cv2.line(frame, (width//2, 0), (width//2, height), WHITE, 1)  #dikey eksen
    cv2.circle(frame, (ccx, ccy), 3, RED, -1)   #pencerenin merkezi
    cv2.polylines(frame, [center_area], isClosed=True, color=RED, thickness=2)  #hedefin olmasını istediğimiz konumu

    cv2.imshow("mask", mask)
    cv2.imshow("project", frame)

cap.release()
cv2.destroyAllWindows()