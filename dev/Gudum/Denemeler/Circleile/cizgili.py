import cv2
import numpy as np
import time

# Kamera akışını başlat
cap = cv2.VideoCapture(0)

# Son tespit edilen dairenin merkezi ve yarıçapı
last_center = None
last_radius = -1

# Arka arkaya aynı daireyi tespit etme sayacı
counter = 0

# Çizgilerin aralığı (5 cm)
line_spacing = 20  # Piksel cinsinden

# Çizgilerin kesişim noktalarını saklamak için boş bir liste oluşturun
intersection_points = []

# Uzak mesafe için kernel ve iterasyon değerleri
kernel_erode = np.ones((0, 0), np.uint8)
kernel_dilate = np.ones((3, 3), np.uint8)
kernel_width = 4
kernel_height = 2

# Ortalama kernel ve iterasyon değerleri
kernel_avg = np.ones((10, 10), np.uint8)
erode_avg = 2
dilate_avg = 5

# Kernel ve iterasyon değerlerini geçiçi olarak saklayın
temp_kernel = kernel_avg
temp_erode = erode_avg
temp_dilate = dilate_avg

# Başlangıç zamanını kaydedin
start_time = time.time()

# Kernel durumu
kernel_status = "none"

while True:
    # Kameradan kare oku
    ret, frame = cap.read()
    if not ret:
        break

    # Belirli bir süre boyunca farklı kernel değerleri ile daire araması yapın
    elapsed_time = time.time() - start_time
    if elapsed_time % 10 < 5:
        if kernel_status != "far":
            print("Uzak kernel ile aranıyor")
            kernel_status = "far"
        # Uzak mesafe için kernel ve iterasyon değerlerini ayarlayın
        temp_kernel = np.ones((kernel_height, kernel_width), np.uint8)
        temp_erode = 0
        temp_dilate = 3
    else:
        if kernel_status != "average":
            print("Orta kernel ile aranıyor")
            kernel_status = "average"
        # Ortalama kernel ve iterasyon değerlerini kullanın
        temp_kernel = kernel_avg
        temp_erode = erode_avg
        temp_dilate = dilate_avg
        
    # BGR'dan HSV'ye dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı renk için alt ve üst sınırları belirle
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    # Kırmızı renkli alanları maskele
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Gürültüyü azalt
    mask = cv2.erode(mask, temp_kernel, iterations=temp_erode)
    mask = cv2.dilate(mask, kernel_dilate, iterations=temp_dilate)

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
            if counter == 1:
                print("Uzak kernelde görüntü yakalandı ve takip ediliyor")
        else:
            counter = 0
            if last_center is not None and max_center is None:
                print("Görüntü kaybedildi")
    else:
        counter = 0
        if last_center is not None and max_center is None:
            print("Görüntü kaybedildi")

    last_center = max_center
    last_radius = max_radius

    # 15 frame boyunca aynı daire görünüyorsa, daire çiz
    if counter >= 5:
        cv2.circle(frame, last_center, int(last_radius), (0, 255, 0), 2)

    # Yatay ve dikey çizgileri çiz
    for i in range(0, frame.shape[0], line_spacing):
        cv2.line(frame, (0, i), (frame.shape[1], i), (0, 255, 0), 1)
    for j in range(0, frame.shape[1], line_spacing):
        cv2.line(frame, (j, 0), (j, frame.shape[0]), (0, 255, 0), 1)

    # Çizgilerin kesişim noktalarını hesaplayın
    if len(intersection_points) < 25:
        intersection_points.clear()
        for i in range(0, frame.shape[0], line_spacing):
            for j in range(0, frame.shape[1], line_spacing):
                intersection_points.append((j, i))

    # Kesişim noktalarını sayın
    count = 0
    for point in intersection_points:
        x, y = point
        if mask[y, x] > 0:
            count += 1

    # Eğer 10 noktadan fazlası kırmızı içeriyorsa "cisim ortada" yazısını görüntüye ekleyin
    if count >= 10:
        cv2.putText(frame, "Cisim Orada", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Sonuçları göster
    cv2.imshow('Kırmızı Daire Tespiti', frame)
    cv2.imshow('Mask', mask)

    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
