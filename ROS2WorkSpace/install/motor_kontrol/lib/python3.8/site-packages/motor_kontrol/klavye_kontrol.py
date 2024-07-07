import rclpy
from rclpy.node import Node
from sobat_interfaces.msg import SobatHareket
from pynput import keyboard

class DirectionPublisher(Node):

    def __init__(self):
        super().__init__('direction_publisher')
        self.publisher_ = self.create_publisher(SobatHareket, '/motor', 10)
        self.current_direction = SobatHareket()
        self.current_direction.ileri = False
        self.current_direction.geri = False
        self.current_direction.sag = False
        self.current_direction.sol = False
        self.current_direction.yukari = False
        self.current_direction.asagi = False

    def on_press(self, key):
        try:
            if key.char == 'w':
                self.update_direction(ileri=True)
            elif key.char == 's':
                self.update_direction(geri=True)
            elif key.char == 'd':
                self.update_direction(sag=True)
            elif key.char == 'a':
                self.update_direction(sol=True)
            elif key.char == 'u':
                self.update_direction(yukari=True)
            elif key.char == 'j':
                self.update_direction(asagi=True)
        except AttributeError:
            pass

    def on_release(self, key):
        self.update_direction()

    def update_direction(self, ileri=False, geri=False, sag=False, sol=False, yukari=False, asagi=False):
        self.current_direction.ileri = ileri
        self.current_direction.geri = geri
        self.current_direction.sag = sag
        self.current_direction.sol = sol
        self.current_direction.yukari = yukari
        self.current_direction.asagi = asagi
        self.publisher_.publish(self.current_direction)
        self.get_logger().info(f'Publishing: {self.current_direction}')

def main(args=None):
    rclpy.init(args=args)
    direction_publisher = DirectionPublisher()

    listener = keyboard.Listener(
        on_press=direction_publisher.on_press,
        on_release=direction_publisher.on_release)
    listener.start()

    try:
        rclpy.spin(direction_publisher)
    except KeyboardInterrupt:
        pass

    direction_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

