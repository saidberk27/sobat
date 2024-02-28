import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String, Float32

class MesafeKontrolNode(Node):
    def __init__(self):
        super().__init__('mesafe_kontrol_node')
        qos_profile = QoSProfile(depth=10)  # Configure desired QoS profile
        self.subscriber_ = self.create_subscription(Float32, '/mesafe2', self.mesafe_callback, qos_profile=qos_profile)
        self.publisher_ = self.create_publisher(String, '/topic_out', 10)

    def mesafe_callback(self, msg):
        try:
            mesafe = float(msg.data)
        except ValueError:
            self.get_logger().error("Geçersiz mesafe değeri: {}".format(msg.data))
            return

        if mesafe > 10:
            yayin_mesaji = "İLERLE"
        else:
            yayin_mesaji = "DUR"

        msg_out = String()
        msg_out.data = yayin_mesaji
        self.publisher_.publish(msg_out)
        self.get_logger().info("Yayınlanan mesaj: {}".format(msg_out.data))

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MesafeKontrolNode()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
