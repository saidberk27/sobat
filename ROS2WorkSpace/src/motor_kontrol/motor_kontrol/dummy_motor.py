import rclpy
from rclpy.node import Node
from sobat_interfaces.msg import SobatHareket

class DirectionPublisher(Node):

    def __init__(self):
        super().__init__('direction_publisher')
        self.publisher_ = self.create_publisher(SobatHareket, '/motor', 10)
        self.timer = self.create_timer(2.0, self.timer_callback)
        self.directions = ['ileri', 'geri', 'sag', 'sol', 'yukari', 'asagi']
        self.current_direction = 0

    def timer_callback(self):
        msg = SobatHareket()
        msg.ileri = False
        msg.geri = False
        msg.sag = False
        msg.sol = False
        msg.yukari = False
        msg.asagi = False
        
        direction = self.directions[self.current_direction]
        setattr(msg, direction, True)
        
        self.publisher_.publish(msg)
        
        self.current_direction = (self.current_direction + 1) % len(self.directions)
        self.get_logger().info(f'Publishing: {msg}')

def main(args=None):
    rclpy.init(args=args)
    direction_publisher = DirectionPublisher()
    rclpy.spin(direction_publisher)
    direction_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
