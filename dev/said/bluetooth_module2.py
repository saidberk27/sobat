import serial
from pymavlink import mavutil
import time

class SubmarineControl:
    def __init__(self, pixhawk_port='/dev/ttyACM0', bluetooth_port='/dev/ttyUSB0', baud_rate=9600):
        self.pixhawk = mavutil.mavlink_connection(pixhawk_port, baud=115200)
        self.bluetooth = serial.Serial(bluetooth_port, baud_rate, timeout=1)
        self.motor_speed = 750
        self.wait_heartbeat()
        self.arm_vehicle()
        self.set_mode('STABILIZE')

    def wait_heartbeat(self):
        print("Waiting for heartbeat...")
        self.pixhawk.wait_heartbeat()
        print("Heartbeat received!")

    def arm_vehicle(self):
        self.pixhawk.arducopter_arm()
        self.pixhawk.motors_armed_wait()
        print("Vehicle armed")

    def set_mode(self, mode):
        if mode not in self.pixhawk.mode_mapping():
            print(f'Unknown mode: {mode}')
            return False
        mode_id = self.pixhawk.mode_mapping()[mode]
        self.pixhawk.set_mode(mode_id)
        print(f"Mode set to {mode}")
        return True

    def move(self, x, y, z, r):
        self.pixhawk.mav.manual_control_send(
            self.pixhawk.target_system,
            x, y, z, r, 0
        )

    def set_servo_pwm(self, servo_number, pwm_value):
        self.pixhawk.mav.command_long_send(
            self.pixhawk.target_system, self.pixhawk.target_component,
            mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
            0, servo_number, pwm_value, 0, 0, 0, 0, 0
        )
        print(f"Setting servo {servo_number} to PWM {pwm_value}")

    def process_bluetooth_data(self):
        while True:
            if self.bluetooth.in_waiting > 0:
                command = self.bluetooth.read().decode('utf-8')
                print(f"Received command: {command}")

                if command == '3':
                    self.move(self.motor_speed, 0, 0, 0)  # İleri
                elif command == '4':
                    self.move(-self.motor_speed, 0, 0, 0)  # Geri
                elif command == '6':
                    self.move(0, -self.motor_speed, 0, 0)  # Sola
                elif command == '5':
                    self.move(0, self.motor_speed, 0, 0)  # Sağa
                elif command == '1':
                    self.move(0, 0, self.motor_speed, 0)  # Yukarı
                elif command == '2':
                    self.move(0, 0, -self.motor_speed, 0)  # Aşağı
                elif command == '0':
                    self.set_servo_pwm(1, 1000)  # Servo 0 derece
                elif command == '45':
                    self.set_servo_pwm(1, 1250)  # Servo 45 derece
                elif command == '90':
                    self.set_servo_pwm(1, 1500)  # Servo 90 derece
                elif command == '135':
                    self.set_servo_pwm(1, 1750)  # Servo 135 derece
                elif command == '180':
                    self.set_servo_pwm(1, 2000)  # Servo 180 derece
                else:
                    self.move(0, 0, 0, 0)  # Hareket yok

            time.sleep(0.1)  # Kısa bir bekleme süresi

    def run(self):
        try:
            self.process_bluetooth_data()
        except KeyboardInterrupt:
            print("Program interrupted by user")
        finally:
            self.move(0, 0, 0, 0)  # Tüm hareketleri durdur
            self.pixhawk.arducopter_disarm()
            print("Vehicle disarmed")

if __name__ == "__main__":
    submarine = SubmarineControl()
    submarine.run()