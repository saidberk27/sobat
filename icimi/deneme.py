import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    # Görüntüyü ters çevir
    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        area = cv2.contourArea(c)
        if area > 5000:
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)

            M = cv2.moments(c)

            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                # Get the center of the frame
                frame_center_x = frame.shape[1] // 2
                frame_center_y = frame.shape[0] // 2

                # Calculate the offset from the frame center
                offset_x = frame_center_x - cx
                offset_y = frame_center_y - cy

                # Determine the instructions based on the position of the centroid
                instructions = []
                if offset_x > 0:
                    instructions.append("Move the shape to the right.")
                elif offset_x < 0:
                    instructions.append("Move the shape to the left.")
                if offset_y > 0:
                    instructions.append("Move the shape down.")
                elif offset_y < 0:
                    instructions.append("Move the shape up.")

                # Print the instructions
                if instructions:
                    print(" ".join(instructions) + " to center the shape.")
                else:
                    print("The shape is centered.")

                cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
                cv2.putText(frame,"Blue",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,2.5,(255,255,255),3)

    cv2.imshow("result", frame)

    k = cv2.waitKey(5)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
