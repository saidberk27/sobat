# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import cv2
import numpy as np
import imutils


import rclpy
from rclpy.node import Node

from std_msgs.msg import String

cap = cv2.VideoCapture(0)
error_margin = 30
previous_centered_message = False  # Flag to store the previous "The shape is approximately centered." message


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        global previous_centered_message

        _, frame = cap.read()

        # Flip the image
        frame = cv2.flip(frame, 1)

        # Get the center of the frame
        frame_center_x = frame.shape[1] // 2
        frame_center_y = frame.shape[0] // 2

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_blue = np.array([90, 50, 50])  # Adjust the hue lower bound as needed
        upper_blue = np.array([130, 255, 255])  # Adjust the hue upper bound as needed


        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # Find the largest contour
        max_contour = max(cnts, key=cv2.contourArea, default=None)
    
        if max_contour is not None:
            area = cv2.contourArea(max_contour)
            if area > 5000:
                cv2.drawContours(frame, [max_contour], -1, (0, 255, 0), 3)

                M = cv2.moments(max_contour)

                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])

                    # Calculate the offset from the frame center
                    offset_x = frame_center_x - cx
                    offset_y = frame_center_y - cy

                    # Calculate the Euclidean distance between the center of the frame and the centroid of the blue region
                    euclidean_distance = np.sqrt(offset_x**2 + offset_y**2)

                    # Calculate the motor speed based on the distance
                    max_distance = np.sqrt(frame_center_x**2 + frame_center_y**2)
                    speed_ratio = euclidean_distance / max_distance
                    motor_speed = int(speed_ratio * 100)  # You can adjust the scaling factor as needed

                    # Calculate the object size (assuming the object is approximately circular)
                    object_size = np.sqrt(area / np.pi)

                    # Check if the offset is within the allowed error range
                    if abs(offset_x) < error_margin and abs(offset_y) < error_margin:
                        motor_speed = 0  # Stop the motors
                        # If the previous "The shape is approximately centered." message was sent, don't send it again
                        if not previous_centered_message:
                            print("The shape is approximately centered.")
                            previous_centered_message = True
                    else:
                        # If the previous "The shape is approximately centered." message was sent, reset the flag
                        if previous_centered_message:
                            previous_centered_message = False


                    # Draw a cross at the center of the frame
                    cv2.line(frame, (frame_center_x - 10, frame_center_y), (frame_center_x + 10, frame_center_y),
                            (255, 255, 255), 2)
                    cv2.line(frame, (frame_center_x, frame_center_y - 10), (frame_center_x, frame_center_y + 10),
                            (255, 255, 255), 2)

                    # Draw a line from the centroid of the blue region to the center of the frame
                    cv2.line(frame, (cx, cy), (frame_center_x, frame_center_y), (255, 255, 255), 2)

                    cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
                    cv2.putText(frame, "Blue", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 255, 255), 3)

                    # Display the Euclidean distance, motor speed, and object size on the frame
                    cv2.putText(frame, f"Distance: {euclidean_distance:.2f} | Speed: {motor_speed} | Object Size: {object_size:.2f}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("result", frame)

        k = cv2.waitKey(5)
        msg = String()

        try:
            msg.data = '{}'.format(offset_x)

        except UnboundLocalError:
            msg.data = 'İlk Tespit Gerçekleşmedi'

   
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):


    error_margin = 30
    previous_instructions = []  # List to store previous instructions
    previous_centered_message = False  # Flag to store the previous "The shape is approximately centered." message

    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)
    
    
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
