import rclpy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from trackbarOptions import *

class CameraSubscriber:
    def __init__(self):
        self.node = rclpy.create_node('camera_subscriber')
        self.bridge = CvBridge()
        self.subscription = self.node.create_subscription(
            Image,
            '/camera/image_raw',  # Bu konumu Gazebo simülasyonunuza göre güncelleyin
            self.image_callback,
            10)
        self.subscription  # Prevent unused variable warning

    def image_callback(self, msg):

        cap_w, cap_h = 1920, 1080

        try:
            frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_warped = warp_finder(frame)
            frame_blur = cv2.GaussianBlur(frame_warped, (5, 5), 15)
            mask = hsv_finder(frame_blur)
            mask = cv2.dilate(mask, np.ones((5, 5), np.uint8), iterations=2)

            _, threshold = cv2.threshold(mask, 100, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            cv2.line(frame, (cap_w // 2, cy), (10, 15), (255, 0, 0), 6)
            mx, my, marea = 0, 0, 0
            for contour in contours:
                if cv2.contourArea(contour) > 79000:
                    cv2.drawContours(frame, [contour], 0, (0, 255, 0), cv2.FILLED)
                    M = cv2.moments(contour)
                    mx += M["m10"]
                    my += M["m01"]
                    marea += M["m00"]

            if marea != 0:
                cx, cy = int(mx / marea), int(my / marea)
                 # cv2.circle(frame_warped, (cx, cy), 8, (0, 0, 255), -1)
                cv2.line(frame, (cap_w // 2, cy), (cx, cy), (255, 0, 0), 6)
                cv2.line(frame, (cap_w//2, 0), (cap_w//2, cap_h), (0, 0, 255), 6)

            cv2.imshow("Gazebo Camera", frame)
            cv2.waitKey(1)
        except Exception as e:
            print(e)

def main(args=None):
    rclpy.init(args=args)
    camera_subscriber = CameraSubscriber()
    rclpy.spin(camera_subscriber.node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

