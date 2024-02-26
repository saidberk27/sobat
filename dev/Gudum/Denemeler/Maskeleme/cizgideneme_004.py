import cv2
import numpy as np
import time

# Kamera akışını başlat
cap = cv2.VideoCapture(0)

# Çizgilerin aralığı (örneğin, her 20 pikselde bir)
line_spacing = 20

# Uzak ve orta kernel ayarları
kernel_far = np.ones((5, 5), np.uint8)  # Uzak nesneler için büyük kernel
kernel_medium = np.ones((3, 3), np.uint8)  # Orta mesafe nesneler için orta boyut kernel

# Nesnenin son durumu, tespit sayacı ve son tespit zamanı
last_status = None
detection_counter = 0
last_detection_time = time.time()

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

            # Nesnenin çerçevedeki boyutunu hesapla
            area = cv2.contourArea(largest_contour)
            # Nesnenin boyutuna göre yakınlık/uzaklık hesapla ve kernel ayarla
            if area > 5000:  # Bu değer deneyimle ayarlanmalıdır
                distance = "Orta"
                kernel = kernel_medium
                if last_status != "Orta":
                    if last_status == "Uzak":
                        print("Uzaktan orta mesafeye geçti.")
                    print("Orta mesafe kerneli kullanılıyor.")
                    last_status = "Orta"
            else:
                distance = "Uzak"
                kernel = kernel_far
                if last_status != "Uzak":
                    print("Uzak mesafe kerneli kullanılıyor.")
                    last_status = "Uzak"

            detection_counter += 1
            last_detection_time = time.time()

            if detection_counter == 10:
                print(f"{last_status} mesafede nesne tespit edildi ve takip ediliyor.")
                detection_counter = 0  # Sayaç sıfırlanır

            # Uzaklık bilgisini ekrana yazdır
            cv2.putText(frame, distance, (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            # Gürültüyü azalt
            mask = cv2.erode(mask, kernel, iterations=2)
            mask = cv2.dilate(mask, kernel, iterations=2)
    else:
        # Eğer 2 saniye içinde nesne tespit edilmezse
        if time.time() - last_detection_time > 2:
            print("Hedef kaybedildi.")
            detection_counter = 0
            last_detection_time = time.time()

    # Yatay çizgileri çiz
    for i in range(0, frame.shape[0], line_spacing):
        cv2.line(frame, (0, i), (frame.shape[1], i), (0, 255, 0), 1)

    # Sonuçları göster
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)

    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
