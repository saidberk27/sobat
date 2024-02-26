import cv2
import numpy as np
import time

def get_direction(center, frame_center):
    horizontal = "Sag" if center[0] > frame_center[0] else "Sol"
    vertical = "Alt" if center[1] > frame_center[1] else "Ust"
    return f"{vertical} {horizontal}"

# Kamera akışını başlat
cap = cv2.VideoCapture(0)

# Uzak ve orta kernel ayarları
kernel_far = np.ones((5, 5), np.uint8)
kernel_medium = np.ones((3, 3), np.uint8)

last_status = None
detection_counter = 0
last_detection_time = time.time()
previous_direction = None
tracking_message_shown = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_center = (frame.shape[1] // 2, frame.shape[0] // 2)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(largest_contour)
        if M["m00"] != 0:
            cx, cy = int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])
            area = cv2.contourArea(largest_contour)
            current_status = "Orta" if area > 5000 else "Uzak"
            if last_status != current_status:
                print(f"{current_status} mesafe kerneli kullanılıyor.")
                last_status = current_status
                tracking_message_shown = False

            detection_counter += 1
            last_detection_time = time.time()

            if detection_counter == 10 and not tracking_message_shown:
                print(f"{last_status} mesafede nesne tespit edildi ve {last_status} kerneli ile takip ediliyor.")
                tracking_message_shown = True
                detection_counter = 0

            direction = get_direction((cx, cy), frame_center)
            if previous_direction != direction:
                print(f"Hedefe doğru gitmek için {direction} noktasına gidiliyor.")
                previous_direction = direction

            cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)
            cv2.putText(frame, direction, (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            mask = cv2.erode(mask, kernel_far if current_status == "Uzak" else kernel_medium, iterations=2)
            mask = cv2.dilate(mask, kernel_far if current_status == "Uzak" else kernel_medium, iterations=2)
    else:
        if time.time() - last_detection_time > 2 and detection_counter > 0:
            print("Hedef kaybedildi.")
            detection_counter = 0
            previous_direction = None
            tracking_message_shown = False
            last_detection_time = time.time()

    # Ekranı yatay ve dikey olarak kes
    cv2.line(frame, (frame_center[0], 0), (frame_center[0], frame.shape[0]), (255, 0, 0), 2)
    cv2.line(frame, (0, frame_center[1]), (frame.shape[1], frame_center[1]), (255, 0, 0), 2)

    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
