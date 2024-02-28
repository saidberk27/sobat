import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
import random

class DummyMesafeSensoruNode(Node):

    def __init__(self):
        super().__init__('dummy_mesafe_sensoru')
        self.publisher_ = self.create_publisher(Float32, 'mesafe2', 10)
        self.timer_ = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        msg = Float32()
        msg.data = random.uniform(0.0, 20.0)  # Mesafe aralığı 0 - 10 metre olarak belirlenmiştir.
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    dummy_mesafe_sensoru_node = DummyMesafeSensoruNode()

    rclpy.spin(dummy_mesafe_sensoru_node)

    dummy_mesafe_sensoru_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
