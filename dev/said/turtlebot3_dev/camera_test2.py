import rclpy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from trackbarOptions import *


class LineDetector:
    def __init__(self):
        self.node = rclpy.create_node('line_detector')
        self.bridge = CvBridge()
        self.subscription = self.node.create_subscription(
            Image,
            '/camera/image_raw',  # Update this according to your Gazebo simulation
            self.image_callback,
            10)
        self.subscription  # Prevent unused variable warning

    def image_callback(self, msg):

        cap_w, cap_h = 1920, 1080
        try:
            frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            #print(frame.shape[1])
            cv2.imshow("frrrrr", frame)
            frame_warped = warp_finder(frame)
            frame_blur = cv2.GaussianBlur(frame_warped, (5, 5), 15)
            mask = hsv_finder(frame_blur)
            mask = cv2.dilate(mask, np.ones((5, 5), np.uint8), iterations=2)

            _, threshold = cv2.threshold(mask, 100, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            mx, my, marea = 0, 0, 0
            for contour in contours:
                if cv2.contourArea(contour):
                    cv2.drawContours(frame_warped, [contour], 0, (0, 255, 0), cv2.FILLED)
                    M = cv2.moments(contour)
                    mx += M["m10"]
                    my += M["m01"]
                    marea += M["m00"]
            print(marea)
            if marea != 0:
                cx, cy = int(mx / marea), int(my / marea)
                cv2.line(frame_warped, (cap_w // 2, cy), (cx, cy), (255, 0, 0), 6)
                if cx <= (cap_w//2) + 40 and cx >= (cap_w//2) - 40:
                    print("Merkez Nokta")
                print(cap_w)
                print(cx)

            # Display the image
                
            cv2.imshow("mask", mask)
            cv2.imshow("Gazebo Camera with Line Detection", frame_warped)
            cv2.waitKey(1)
        except Exception as e:
            print(e)

def main(args=None):
    print("Başlıyor...")
    rclpy.init(args=args)
    line_detector = LineDetector()
    rclpy.spin(line_detector.node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
