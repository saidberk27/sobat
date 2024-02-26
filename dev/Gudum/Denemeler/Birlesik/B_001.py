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

    # Kırmızı renkli alanları maskele (İlk Yöntem)
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    # Gürültüyü azalt
    kernel = np.ones((3, 3), np.uint8)
    mask1 = cv2.erode(mask1, kernel, iterations=2)
    mask1 = cv2.dilate(mask1, kernel, iterations=2)

    # Konturları bul (İlk Yöntem)
    contours1, _ = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # En büyük konturu bul (İlk Yöntem)
    if contours1:
        largest_contour1 = max(contours1, key=cv2.contourArea)
        M = cv2.moments(largest_contour1)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            # Merkezde bir nokta çiz (İlk Yöntem)
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

    # Kırmızı renk için alt ve üst sınırları belirle (İkinci Yöntem)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    # Kırmızı renkli alanları maskele (İkinci Yöntem)
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    # Gürültüyü azalt
    mask2 = cv2.erode(mask2, kernel, iterations=2)
    mask2 = cv2.dilate(mask2, kernel, iterations=2)

    # Konturları bul (İkinci Yöntem)
    contours2, _ = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # En büyük konturu bul (İkinci Yöntem)
    if contours2:
        largest_contour2 = max(contours2, key=cv2.contourArea)
        M = cv2.moments(largest_contour2)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            # Merkezde bir nokta çiz (İkinci Yöntem)
            cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

    # Sonuçları göster (İlk Yöntem)
    cv2.imshow('Kırmızı Daire Tespiti (İlk Yöntem)', frame)
    cv2.imshow('Mask (İlk Yöntem)', mask1)

    # Sonuçları göster (İkinci Yöntem)
    cv2.imshow('Kırmızı Daire Tespiti (İkinci Yöntem)', frame.copy())
    cv2.imshow('Mask (İkinci Yöntem)', mask2)

    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
