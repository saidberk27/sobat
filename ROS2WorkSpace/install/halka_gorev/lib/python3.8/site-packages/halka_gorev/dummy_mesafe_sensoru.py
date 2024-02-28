import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile

from sobat_interfaces.msg import MesafeSensor

import random

class DummyMesafeSensoruNode(Node):

    def __init__(self):
        super().__init__('dummy_mesafe_sensoru')
        qos_profile = QoSProfile(depth=10)
        self.publisher_ = self.create_publisher(MesafeSensor, '/mesafe_sensor', 10)
        self.timer_ = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        msg = MesafeSensor()
        msg.mesafe_sensor1 = random.uniform(0.0, 20.0)
        msg.mesafe_sensor2 = random.uniform(0.0, 20.0)
        msg.mesafe_sensor3 = random.uniform(0.0, 20.0)
        msg.mesafe_sensor4 = random.uniform(0.0, 20.0)
        msg.mesafe_sensor5 = random.uniform(0.0, 20.0)

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    dummy_mesafe_sensoru_node = DummyMesafeSensoruNode()

    rclpy.spin(dummy_mesafe_sensoru_node)

    dummy_mesafe_sensoru_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
