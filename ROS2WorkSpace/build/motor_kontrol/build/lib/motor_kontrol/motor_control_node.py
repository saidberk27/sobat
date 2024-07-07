#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sobat_interfaces.msg import SobatHareket
from pymavlink import mavutil
import time

class MotorKontrol(Node):
    def __init__(self):
        super().__init__('motor_kontrol_node')
        self.subscription = self.create_subscription(
            SobatHareket,
            '/motor',
            self.motor_callback,
            10)
        self.subscription  # prevent unused variable warning
        
        self.pixhawk_port = '/dev/ttyACM0'
        self.motor_hiz = 750
        try:
            self.master = mavutil.mavlink_connection(self.pixhawk_port, baud=115200)
            self.getHeartBeat()
            self.armPixHawk()
        except Exception as e:
            self.get_logger().error(f"Port Kapali: {str(e)}")

    def getHeartBeat(self):
        try:
            self.master.wait_heartbeat()
            self.get_logger().info("Kalp Atisi")
        except Exception as e:
            self.get_logger().error(f"Port Kapali: {str(e)}")

    def armPixHawk(self):
        try:
            self.master.mav.command_long_send(
                self.master.target_system,
                self.master.target_component,
                mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
                0,
                1, 0, 0, 0, 0, 0, 0)
            self.get_logger().info("Waiting for the vehicle to arm")
            self.master.motors_armed_wait()
            self.get_logger().info('Armed!')
        except Exception as e:
            self.get_logger().error(f"Port Kapali: {str(e)}")

    def move(self, x, y, z, r, duration):
        start_time = time.time()
        while time.time() - start_time < duration:
            self.master.mav.manual_control_send(
                self.master.target_system,
                x, y, z, r, 0
            )
            self.get_logger().info(f"Hareket: x={x}, y={y}, z={z}, r={r}")
            time.sleep(0.1)  # Short delay to prevent flooding

    def motor_callback(self, msg):
        try:
            if msg.ileri:
                self.ileri_git()
            elif msg.geri:
                self.geri_git()
            elif msg.sag:
                self.saga_git()
            elif msg.sol:
                self.sola_git()
            elif msg.yukari:
                self.yukari_git()
            elif msg.asagi:
                self.asagi_git()
            else:
                self.dur()
        except Exception as e:
            self.get_logger().error(f"Hata: {e}")

    def ileri_git(self):
        self.get_logger().info("İleri gidiliyor")
        self.move(self.motor_hiz, 0, 0, 0, 3)

    def geri_git(self):
        self.get_logger().info("Geri gidiliyor")
        self.move(-self.motor_hiz, 0, 0, 0, 3)

    def saga_git(self):
        self.get_logger().info("Sağa gidiliyor")
        self.move(0, self.motor_hiz, 0, 0, 3)

    def sola_git(self):
        self.get_logger().info("Sola gidiliyor")
        self.move(0, -self.motor_hiz, 0, 0, 3)

    def yukari_git(self):
        self.get_logger().info("Yukarı gidiliyor")
        self.move(0, 0, self.motor_hiz, 0, 3)

    def asagi_git(self):
        self.get_logger().info("Aşağı gidiliyor")
        self.move(0, 0, -self.motor_hiz, 0, 3)

    def dur(self):
        self.get_logger().info("Durdu")
        self.move(0, 0, 0, 0, 1)

def main(args=None):
    rclpy.init(args=args)
    motor_kontrol = MotorKontrol()
    rclpy.spin(motor_kontrol)
    motor_kontrol.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()