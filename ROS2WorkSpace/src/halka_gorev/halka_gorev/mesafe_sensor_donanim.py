import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range

import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from DFRobot_RaspberryPi_A02YYUW import DFRobot_A02_Distance as Board

BOARD = Board()  # Create a global instance of the board object

class DistancePublisher(Node):

    def __init__(self):
        super().__init__('distance_publisher')
        self.publisher = self.create_publisher(Range, 'distance', 10)

        # Set sensor range limits
        dis_min = 0
        dis_max = 4500
        BOARD.set_dis_range(dis_min, dis_max)

        self.timer = self.create_timer(0.3, self.publish_distance)  # Timer for periodic publishing

    def publish_distance(self):
        distance = BOARD.getDistance()
        message = Range()
        message.header.stamp = self.get_clock().now().to_msg()
        message.header.frame_id = 'distance_sensor'  # Set appropriate frame ID
        message.radiation_type = Range.INFRARED  # Specify sensor type
        message.field_of_view = 0.7  # Approximate field of view (radians)
        message.min_range = dis_min
        message.max_range = dis_max
        message.range = distance

        if BOARD.last_operate_status == BOARD.STA_OK:
            self.publisher.publish(message)
        else:
            self.get_logger().error("Distance sensor error: %s", BOARD.last_operate_status)

def main(args=None):
    rclpy.init(args=args)
    distance_publisher = DistancePublisher()
    rclpy.spin(distance_publisher)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
