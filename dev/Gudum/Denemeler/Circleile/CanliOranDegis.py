import cv2
import numpy as np
import tkinter as tk
from tkinter import *
import threading

def update_noise_reduction(_=None):
    pass

def process_camera_stream():
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (500, 500))
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_red, upper_red)
        kernel = np.ones((kernel_height.get(), kernel_width.get()), np.uint8)
        temp_mask = cv2.erode(mask, kernel, iterations=erode_iter.get())
        temp_mask = cv2.dilate(temp_mask, kernel, iterations=dilate_iter.get())
        contours, _ = cv2.findContours(temp_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 100:
                perimeter = cv2.arcLength(contour, True)
                if perimeter == 0:
                    continue
                circularity = 4 * np.pi * (area / (perimeter * perimeter))
                if 0.7 < circularity < 1.2:
                    (x, y), radius = cv2.minEnclosingCircle(contour)
                    center = (int(x), int(y))
                    radius = int(radius)
                    cv2.circle(frame, center, radius, (0, 255, 0), 2)

        cv2.imshow('Kırmızı Daire Tespiti', frame)
        cv2.imshow('Mask', temp_mask)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

root = tk.Tk()
erode_iter = IntVar(value=2)
dilate_iter = IntVar(value=5)
kernel_width = IntVar(value=2)
kernel_height = IntVar(value=1)

lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

Label(root, text='Erode Iterations').pack()
Scale(root, from_=0, to=10, orient=HORIZONTAL, variable=erode_iter, command=update_noise_reduction).pack()

Label(root, text='Dilate Iterations').pack()
Scale(root, from_=0, to=10, orient=HORIZONTAL, variable=dilate_iter, command=update_noise_reduction).pack()

Label(root, text='Kernel Width').pack()
Scale(root, from_=0, to=50, orient=HORIZONTAL, variable=kernel_width, command=update_noise_reduction).pack()

Label(root, text='Kernel Height').pack()
Scale(root, from_=0, to=50, orient=HORIZONTAL, variable=kernel_height, command=update_noise_reduction).pack()

cap = cv2.VideoCapture(0)

# Kamera işlemlerini ayrı bir thread üzerinde çalıştırın
camera_thread = threading.Thread(target=process_camera_stream)
camera_thread.daemon = True
camera_thread.start()

root.mainloop()
cap.release()
cv2.destroyAllWindows()
