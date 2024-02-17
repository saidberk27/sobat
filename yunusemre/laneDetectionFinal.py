# yolo ilk başta 1 seferlik çalıştırılmalı (ilk çalışmada hazırlık yapıyor)

import cv2
import numpy as np
from ultralytics import YOLO
import os
import matplotlib.pyplot as plt
import pandas as pd


def empty(x):
    pass

def options(cap_w, cap_h):
    title = "options"
    cv2.namedWindow(title)
    cv2.resizeWindow(title, (500, 550))

    cv2.createTrackbar("lower_H", title, 0, 179, empty)
    cv2.createTrackbar("lower_S", title, 0, 255, empty)
    cv2.createTrackbar("lower_V", title, 0, 255, empty)
    cv2.createTrackbar("upper_H", title, 0, 179, empty)
    cv2.createTrackbar("upper_S", title, 0, 255, empty)
    cv2.createTrackbar("upper_V", title, 0, 255, empty)

    cv2.createTrackbar("htop", title, 0, cap_h, empty)
    cv2.createTrackbar("wtop", title, 0, cap_w, empty)
    cv2.createTrackbar("hbot", title, 0, cap_h, empty)
    cv2.createTrackbar("wbot", title, 0, cap_w, empty)

def hsv_finder(frame):
    title = "options"
    lower_h = cv2.getTrackbarPos("lower_H", title)
    lower_s = cv2.getTrackbarPos("lower_S", title)
    lower_v = cv2.getTrackbarPos("lower_V", title)
    upper_h = cv2.getTrackbarPos("upper_H", title)
    upper_s = cv2.getTrackbarPos("upper_S", title)
    upper_v = cv2.getTrackbarPos("upper_V", title)
    lower = np.array([lower_h, lower_s, lower_v])
    upper = np.array([upper_h, upper_s, upper_v])
    mask = cv2.inRange(frame, lower, upper)
    return mask

def warp_finder():
    title = "options"
    htop = cv2.getTrackbarPos("htop", title)
    wtop = cv2.getTrackbarPos("wtop", title)
    hbot = cv2.getTrackbarPos("hbot", title)
    wbot = cv2.getTrackbarPos("wbot", title)
    pts = [[cap_w//2 - wtop//2, htop], [cap_w//2 + wtop//2, htop], [cap_w//2 + wbot//2, hbot], [cap_w//2 - wbot//2, hbot]]
    return pts


def getLaneCurves(frame, mask):
    cx = None
    _, threshold = cv2.threshold(mask, 100, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        cv2.drawContours(frame, [max_contour], -1, (0, 255, 0), 2)
        M = cv2.moments(max_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cx, cy), 5, (255, 255, 0), -1)
    cv2.imshow("contours", frame)
    return cx



def warpFrame(frame, pts, cap_w, cap_h):
    pts1 = np.float32(pts)
    pts2 = np.float32([[0, 0], [cap_w, 0], [cap_w, cap_h], [0, cap_h]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    frame_warped = cv2.warpPerspective(frame, matrix, (cap_w, cap_h))
    return frame_warped

def save_photo(file_name, frame):
    if not os.path.exists(file_name):
        cv2.imwrite(file_name, frame)

def shape_detect(frame):
    results = model.predict(frame)
    for result in results:
        for box in result.boxes:
            box_conf = float(box.conf[0])
            box_label_no = int(box.cls[0])
            box_label = model.names[box_label_no]
            if box_conf > 0.85:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
                cv2.putText(frame, box_label, (x1, y1 + 65), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
                cv2.putText(frame, f"{box_label_no}", (x1, y1 + 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
                cv2.putText(frame, f"{box_conf:.2f}", (x1, y1 + 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
                file_name = "../" + box_label + ".jpg"
                save_photo(file_name, frame)




model = YOLO("../yolov8s.pt")
vid = "C:/Users/Yunus Emre/Desktop/vid.mp4"
cap = cv2.VideoCapture(0)

cap_w, cap_h = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

options(cap_w, cap_h)

frame_count = 0
x = []
y = []
plt.style.use('fivethirtyeight')

while True:

    key = cv2.waitKey(15)

    if key & 0xFF == ord('q'):
        break

    scs, frame = cap.read()
    #frame = frame[200:500, 0:cap_w]

    if not scs:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    #cv2.imshow("hsv-values", hsv_finder(frame))


    pts = warp_finder()
    #pts = [[525, 567], [755, 567], [1011, 720], [269, 720]]
    frame_warped = warpFrame(frame, pts, cap_w, cap_h)
    cv2.imshow("frame warped", frame_warped)

    mask = hsv_finder(frame_warped)
    #mask = getLaneCurves(frame)

    frame_masked = cv2.bitwise_and(frame_warped, frame_warped, mask=mask)
    cv2.imshow("frame masked", frame_masked)

    cx = getLaneCurves(frame_warped, mask)
    print(cx)
    frame_count += 1

    if frame_count % 5 == 0:
        x.append(frame_count)
        y.append(cx)
        plt.plot(x, y)

    if key & 0xFF == ord('s'):
        shape_detect(frame)

    for pt in pts:
        cv2.circle(frame, pt, 6, (0, 0, 255), -1)

    cv2.imshow("frame", frame)

    if key & 0xFF == ord('p'):
        cv2.waitKey(0)
        print(pts)


cap.release()
cv2.destroyAllWindows()
plt.tight_layout()
plt.show()
