import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String, Float32, Bool

class HalkaArama(Node):

    def __init__(self):
        super().__init__('halka_arama_node')
        qos_profile = QoSProfile(depth=10)  # Configure desired QoS profile
        self.engel1 = self.create_subscription(Float32, '/engel1', self.mesafe1_callback, qos_profile=qos_profile)
        self.engel2 = self.create_subscription(Float32, '/engel2', self.mesafe2_callback, qos_profile=qos_profile)
        self.engel3 = self.create_subscription(Float32, '/engel3', self.mesafe3_callback, qos_profile=qos_profile)
        self.engel4 = self.create_subscription(Float32, '/engel4', self.mesafe4_callback, qos_profile=qos_profile)
        self.engel5 = self.create_subscription(Float32, '/engel5', self.mesafe5_callback, qos_profile=qos_profile)

        self.publisher_1 = self.create_publisher(Bool, '/engel1', 10)
        self.publisher_2 = self.create_publisher(Bool, '/engel2', 10)
        self.publisher_3 = self.create_publisher(Bool, '/engel3', 10)
        self.publisher_4 = self.create_publisher(Bool, '/engel4', 10)
        self.publisher_5 = self.create_publisher(Bool, '/engel5', 10)

    def mesafe1_callback(self, msg):
        try:
            mesafe = float(msg.data)
        except ValueError:
            self.get_logger().error("Geçersiz mesafe değeri: {}".format(msg.data))
            return

        yayin_mesaji = "SENSOR5 DATA {}".format(mesafe)

        msg_out = Bool()

        msg_out.data = True
        if(mesafe < 10):
            msg_out.data = False

        self.publisher_1.publish(msg_out)
        self.get_logger().info("1 Yayınlanan mesaj: {}".format(msg_out.data))
 
    def mesafe2_callback(self, msg):
        try:
            mesafe = float(msg.data)
        except ValueError:
            self.get_logger().error("Geçersiz mesafe değeri: {}".format(msg.data))
            return

        yayin_mesaji = "SENSOR5 DATA {}".format(mesafe)

        msg_out = Bool()

        msg_out.data = True
        if(mesafe < 10):
            msg_out.data = False

        self.publisher_2.publish(msg_out)
        self.get_logger().info("2 Yayınlanan mesaj: {}".format(msg_out.data))

    def mesafe3_callback(self, msg):
        try:
            mesafe = float(msg.data)
        except ValueError:
            self.get_logger().error("Geçersiz mesafe değeri: {}".format(msg.data))
            return

        yayin_mesaji = "SENSOR5 DATA {}".format(mesafe)

        msg_out = Bool()

        msg_out.data = True
        if(mesafe < 10):
            msg_out.data = False

        self.publisher_3.publish(msg_out)
        self.get_logger().info("3 Yayınlanan mesaj: {}".format(msg_out.data))

    def mesafe4_callback(self, msg):
        try:
            mesafe = float(msg.data)
        except ValueError:
            self.get_logger().error("Geçersiz mesafe değeri: {}".format(msg.data))
            return

        yayin_mesaji = "SENSOR5 DATA {}".format(mesafe)

        msg_out = Bool()

        msg_out.data = True
        if(mesafe < 10):
            msg_out.data = False

        self.publisher_4.publish(msg_out)
        self.get_logger().info("4 Yayınlanan mesaj: {}".format(msg_out.data))

    def mesafe5_callback(self, msg):
        try:
            mesafe = float(msg.data)
        except ValueError:
            self.get_logger().error("Geçersiz mesafe değeri: {}".format(msg.data))
            return

        yayin_mesaji = "SENSOR5 DATA {}".format(mesafe)

        msg_out = Bool()

        msg_out.data = True
        if(mesafe < 10):
            msg_out.data = False

        self.publisher_5.publish(msg_out)
        self.get_logger().info("5 Yayınlanan mesaj: {}".format(msg_out.data))

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = HalkaArama()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
