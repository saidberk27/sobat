import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, captured_frame = cap.read()
    output_frame = captured_frame.copy()

    # Image processing to detect red circles
    captured_frame_bgr = cv2.cvtColor(captured_frame, cv2.COLOR_BGRA2BGR)
    captured_frame_bgr = cv2.medianBlur(captured_frame_bgr, 3)
    captured_frame_lab = cv2.cvtColor(captured_frame_bgr, cv2.COLOR_BGR2Lab)
    captured_frame_lab_red = cv2.inRange(captured_frame_lab, np.array([20, 150, 150]), np.array([190, 255, 255]))
    captured_frame_lab_red = cv2.GaussianBlur(captured_frame_lab_red, (5, 5), 2, 2)
    circles = cv2.HoughCircles(captured_frame_lab_red, cv2.HOUGH_GRADIENT, 1, captured_frame_lab_red.shape[0] / 8, param1=100, param2=18, minRadius=5, maxRadius=60)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for circle in circles:
            # Draw the outer circle
            cv2.circle(output_frame, (circle[0], circle[1]), circle[2], (0, 255, 0), 2)
            # Draw the center of the circle
            cv2.circle(output_frame, (circle[0], circle[1]), 2, (0, 0, 255), 3)
            # Draw horizontal line
            cv2.line(output_frame, (0, circle[1]), (output_frame.shape[1], circle[1]), (255, 0, 0), 2)
            # Draw vertical line
            cv2.line(output_frame, (circle[0], 0), (circle[0], output_frame.shape[0]), (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('frame', output_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
