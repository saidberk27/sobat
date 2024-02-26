import cv2
import numpy as np

# Kamera akışını başlat
cap = cv2.VideoCapture(0)

while True:
    # Kameradan kare oku
    ret, frame = cap.read()
    if not ret:
        break

    # BGR'dan HSV'ye dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı renk için alt ve üst sınırları belirle
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    # Kırmızı renkli alanları maskele
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Gürültüyü azalt
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=2)

    # Konturları bul
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # En büyük konturu bul
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(largest_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            # Merkezde bir nokta çiz
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)


    # Sonuçları göster
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)

    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
