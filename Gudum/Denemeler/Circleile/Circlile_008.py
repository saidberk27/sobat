import cv2
import numpy as np

# Kamera akışını başlat
cap = cv2.VideoCapture(0)

# Kırmızı dairenin konumunu saklamak için değişkenler
x, y, radius = 0, 0, 0

# GOTURN izleme nesnesini oluştur
tracker = cv2.TrackerGOTURN_create()

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
    kernel = np.ones((2, 4), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=0)
    mask = cv2.dilate(mask, kernel, iterations=3)

    # Konturları bul
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Konturlar içinde daire şekillerini tespit et
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:  # Min alanı ayarla
            # Daire benzerliğini kontrol et
            perimeter = cv2.arcLength(contour, True)
            if perimeter == 0:
                continue
            circularity = 4 * np.pi * (area / (perimeter * perimeter))
            if 0.7 < circularity < 1.2:  # Daire benzerliği için eşik değer
                (x, y), radius = cv2.minEnclosingCircle(contour)
                center = (int(x), int(y))
                radius = int(radius)
                # Daire çiz
                cv2.circle(frame, center, radius, (0, 255, 0), 2)

    # Tracker'ı başlat veya güncelle
    if radius > 0:
        success, bbox = tracker.update(frame)

        if success:
            # İzleme başarılıysa, nesnenin yeni konumunu bbox değişkeninde bulabilirsiniz
            x, y, w, h = [int(i) for i in bbox]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Sonuçları göster
    cv2.imshow('Kırmızı Daire Tespiti', frame)
    cv2.imshow('Mask', mask)  # Maskelenmiş görüntüyü göster

    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
