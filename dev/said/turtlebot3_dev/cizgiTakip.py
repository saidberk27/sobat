import cv2
from trackbarOptions import *


path = ""
cap_w, cap_h = 1024, 768

while True:

    frame = cv2.imread(path)
    frame_warped = warp_finder(frame)
    frame_blur = cv2.GaussianBlur(frame_warped, (5, 5), 15)
    mask = hsv_finder(frame_blur)
    mask = cv2.dilate(mask, np.ones((5, 5), np.uint8), iterations=2)

    _, threshold = cv2.threshold(mask, 100, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # max_contour = max(contours, key=cv2.contourArea)

    mx, my, marea = 0, 0, 0
    for contour in contours:
        if cv2.contourArea(contour) > 79000:
            cv2.drawContours(frame_warped, [contour], 0, (0, 255, 0), cv2.FILLED)
            M = cv2.moments(contour)
            mx += M["m10"]
            my += M["m01"]
            marea += M["m00"]




    #all_contours = np.concatenate(filtered_contours) # bu fonksiyon pek sağlıklı çalısmıyor sanırım
    if marea != 0:
        cx, cy = int(mx / marea), int(my / marea)
        # cv2.circle(frame_warped, (cx, cy), 8, (0, 0, 255), -1)
        cv2.line(frame_warped, (cap_w // 2, cy), (cx, cy), (255, 0, 0), 6)
        cv2.line(frame_warped, (cap_w//2, 0), (cap_w//2, cap_h), (0, 0, 255), 6)
        
    cv2.imshow("frame_warped", frame_warped)

    cv2.imshow("mask", mask)
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cv2.destroyAllWindows()