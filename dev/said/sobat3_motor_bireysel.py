import serial
from pymavlink import mavutil
import time


class SubmarineControl:
    def __init__(self, pixhawk_port='/dev/ttyACM0', bluetooth_port='/dev/ttyUSB0'):
        self.pixhawk = mavutil.mavlink_connection(pixhawk_port, baud=115200)
        self.bluetooth = serial.Serial(bluetooth_port, 9600, timeout=1)
        self.last_command = None
        self.movements = [('wait', 7.0), ('forward', 3.0), ('right', 5.0), ('left', 2.0), ('up', 5.0), ('down', 2.0)]

    def arm_vehicle(self):
        self.pixhawk.arducopter_arm()
        print("Vehicle armed")

    def check_arm_status(self):
        self.pixhawk.wait_heartbeat()
        if not self.pixhawk.motors_armed():
            print("Vehicle is disarmed. Re-arming...")
            self.arm_vehicle()
        else:
            print("Vehicle is armed")

    def set_motor_speed(self, motor_number, speed_percent):
        # Convert percent to PWM (assuming 1100-1900 PWM range)
        pwm = 1100 + (speed_percent / 100.0) * 800
        pwm = int(pwm)

        self.pixhawk.mav.command_long_send(
            self.pixhawk.target_system, self.pixhawk.target_component,
            mavutil.mavlink.MAV_CMD_DO_MOTOR_TEST,
            0,  # Confirmation
            motor_number,  # Motor number
            mavutil.mavlink.MOTOR_TEST_THROTTLE_PERCENT,  # Test type
            speed_percent,  # Throttle percentage
            0,  # Timeout (0 for no timeout)
            0, 0, 0  # Unused parameters
        )
        print(f"Setting motor {motor_number} to {speed_percent}% speed (PWM: {pwm})")

    def move(self, motor1_speed, motor2_speed, motor3_speed, motor4_speed):
        self.set_motor_speed(1, motor1_speed)
        self.set_motor_speed(2, motor2_speed)
        self.set_motor_speed(3, motor3_speed)
        self.set_motor_speed(4, motor4_speed)

    def execute_command(self, command):
        if command == "forward":
            self.move(70, 70, 0, 0)  # Örnek: İleri hareket için 1. ve 2. motorları çalıştır
        elif command == "backward":
            self.move(-70, -70, 0, 0)
        elif command == "right":
            self.move(70, -70, 0, 0)
        elif command == "left":
            self.move(-70, 70, 0, 0)
        elif command == "up":
            self.move(0, 0, 70, 70)  # Örnek: Yukarı hareket için 3. ve 4. motorları çalıştır
        elif command == "down":
            self.move(0, 0, -70, -70)
        elif command == "stop":
            self.move(0, 0, 0, 0)
        else:
            print("Geçersiz komut!")

    def otonom(self):
        for movement in self.movements:
            if movement[0] == "wait":
                print(f"{movement[1]} saniye bekleniyor...")
                time.sleep(movement[1])
            else:
                print(f"Hareket: {movement[0]}, Süre: {movement[1]} saniye")
                self.execute_command(movement[0])
                time.sleep(movement[1])
        self.execute_command("stop")

    def read_bluetooth_data(self):
        try:
            while True:
                data = self.bluetooth.read(1).decode('utf-8').strip()
                if data:
                    print(f"Received command: {data}")
                    self.check_arm_status()
                    self.execute_command(data)
                    self.last_command = data
                elif self.last_command:
                    print(f"Re-sending last command: {self.last_command}")
                    self.check_arm_status()
                    self.execute_command(self.last_command)
                time.sleep(0.01)
        except KeyboardInterrupt:
            print("Program stopped.")
        finally:
            if self.bluetooth:
                self.bluetooth.close()

    def run(self):
        try:
            self.pixhawk.wait_heartbeat()
            self.arm_vehicle()
            print("Vehicle armed")
            self.read_bluetooth_data()
        except KeyboardInterrupt:
            print("Program interrupted by user")
        finally:
            print("Vehicle disarmed")
            self.pixhawk.arducopter_disarm()
            self.pixhawk.motors_disarmed_wait()


if __name__ == "__main__":
    submarine = SubmarineControl()
    submarine.run()