import cv2
import numpy as np

def say(x):
    pass

def hsv_prepare(title):
    cv2.namedWindow(title)
    cv2.resizeWindow(title, (960, 720))
    cv2.createTrackbar("lower_H", title, 0, 179, say)
    cv2.createTrackbar("lower_S", title, 0, 255, say)
    cv2.createTrackbar("lower_V", title, 0, 255, say)
    cv2.createTrackbar("upper_H", title, 0, 179, say)
    cv2.createTrackbar("upper_S", title, 0, 255, say)
    cv2.createTrackbar("upper_V", title, 0, 255, say)
    cv2.setTrackbarPos("lower_H", title, 0)
    cv2.setTrackbarPos("lower_S", title, 0)
    cv2.setTrackbarPos("lower_V", title, 0)
    cv2.setTrackbarPos("upper_H", title, 179)
    cv2.setTrackbarPos("upper_S", title, 255)
    cv2.setTrackbarPos("upper_V", title, 255)

def hsv_finder(title, frame):
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