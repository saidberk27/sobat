import cv2
import numpy as np

# Kamera akışını başlat
cap = cv2.VideoCapture(0)

# Son tespit edilen dairenin merkezi ve yarıçapı
last_center = None
last_radius = -1

# Arka arkaya aynı daireyi tespit etme sayacı
counter = 0

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
    kernel = np.ones((10, 10), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=5)

    # Konturları bul
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # En büyük daireyi bul
    max_radius = 0
    max_center = None
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:  # Min alanı ayarla
            (x, y), radius = cv2.minEnclosingCircle(contour)
            if radius > max_radius:
                max_radius = radius
                max_center = (int(x), int(y))

    # Arka arkaya aynı daireyi tespit et
    if max_center is not None and last_center is not None:
        distance = np.sqrt((max_center[0] - last_center[0])**2 + (max_center[1] - last_center[1])**2)
        radius_difference = abs(max_radius - last_radius)

        if distance < 10 and radius_difference < 10:  # Merkez ve yarıçap farkı için eşik değerleri
            counter += 1
        else:
            counter = 0
    else:
        counter = 0

    last_center = max_center
    last_radius = max_radius

    # 15 frame boyunca aynı daire görünüyorsa, daire çiz
    if counter >= 5:
        cv2.circle(frame, last_center, int(last_radius), (0, 255, 0), 2)

    # Sonuçları göster
    cv2.imshow('Kırmızı Daire Tespiti', frame)
    cv2.imshow('Mask', mask)

    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
