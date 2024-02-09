import cv2 as cv
import numpy as np

# Videoyu oku
cap = cv.VideoCapture(0)

# Kamera açılamazsa çık
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Frame yakala
    _, frame = cap.read()

    # Görüntüyü HSV'ye dönüştür
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # kırmızı renk aralığını belirle
    low_red = np.array([161,155,84])
    high_red = np.array([179,255,255])

    # HSV görüntüsünde kırmızı renk aralığına sahip pikselleri maskele
    red_mask = cv.inRange(hsv_frame, low_red, high_red)

    # Maskeyi görüntüye uygula
    red = cv.bitwise_and(frame, frame, mask=red_mask)

    # Sonucu göster
    cv.imshow('frame', frame)
    cv.imshow('red', red)
    cv.imshow('mask', red_mask)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()