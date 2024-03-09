import cv2
import numpy as np

def empty(x):
    pass

# ÖN AYARLAR
cap_w, cap_h = 1920, 1080         # kamera ekranının çözünürlük değerleri
title = "options"
cv2.namedWindow(title)
cv2.resizeWindow(title, (960, 500))

cv2.createTrackbar("lower_H", title, 0, 179, empty)
cv2.createTrackbar("lower_S", title, 0, 255, empty)
cv2.createTrackbar("lower_V", title, 0, 255, empty)
cv2.createTrackbar("upper_H", title, 0, 179, empty)
cv2.createTrackbar("upper_S", title, 0, 255, empty)
cv2.createTrackbar("upper_V", title, 0, 255, empty)

cv2.setTrackbarPos("lower_H", title, 0)
cv2.setTrackbarPos("lower_S", title, 110)
cv2.setTrackbarPos("lower_V", title, 120)
cv2.setTrackbarPos("upper_H", title, 148)
cv2.setTrackbarPos("upper_S", title, 255)
cv2.setTrackbarPos("upper_V", title, 255)

cv2.createTrackbar("h_top", title, 0, cap_h, empty)
cv2.createTrackbar("w_top", title, 0, cap_w, empty)
cv2.createTrackbar("h_bot", title, 0, cap_h, empty)
cv2.createTrackbar("w_bot", title, 0, cap_w, empty)

cv2.setTrackbarPos("h_top", title, 950)
cv2.setTrackbarPos("w_top", title, 1920)
cv2.setTrackbarPos("h_bot", title, 1080)
cv2.setTrackbarPos("w_bot", title, 1920)

def hsv_finder(frame):
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

def warp_finder(frame):
    h_top = cv2.getTrackbarPos("h_top", title)
    w_top = cv2.getTrackbarPos("w_top", title)
    h_bot = cv2.getTrackbarPos("h_bot", title)
    w_bot = cv2.getTrackbarPos("w_bot", title)
    pts1 = np.float32([[cap_w//2 - w_top//2, h_top], [cap_w//2 + w_top//2, h_top], [cap_w//2 + w_bot//2, h_bot], [cap_w//2 - w_bot//2, h_bot]])
    pts2 = np.float32([[0, 0], [cap_w, 0], [cap_w, cap_h], [0, cap_h]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    frame_warped = cv2.warpPerspective(frame, matrix, (cap_w, cap_h))
    return frame_warped
