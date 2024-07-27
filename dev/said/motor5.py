import serial
from pymavlink import mavutil
import time

class SubmarineControl:
    def __init__(self, pixhawk_port='/dev/ttyACM0', bluetooth_port='/dev/ttyUSB0'):
        self.pixhawk = mavutil.mavlink_connection(pixhawk_port, baud=115200)
        self.bluetooth = serial.Serial(bluetooth_port, 9600, timeout=1)
        self.last_command = None
        self.motor_speed = 70  # Default motor speed
        self.movements = [('wait', 7.0), ('c', 3.0), ('f', 5.0), ('e', 2.0), ('a', 5.0), ('b', 2.0)]

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
        pwm = 1100 + (speed_percent / 100.0) * 800
        pwm = int(pwm)

        self.run_cmd(
            mavutil.mavlink.MAV_CMD_DO_MOTOR_TEST,
            p1=motor_number,  # motor instance
            p2=mavutil.mavlink.MOTOR_TEST_THROTTLE_PWM,  # throttle type
            p3=pwm,  # throttle (PWM value)
            p4=5,  # timeout
            p5=1,  # motor count
            p6=0,  # test order (see MOTOR_TEST_ORDER)
        )
        print(f"Setting motor {motor_number} to {speed_percent}% speed (PWM: {pwm})")

    def run_cmd(self, command, p1=0, p2=0, p3=0, p4=0, p5=0, p6=0, p7=0):
        self.pixhawk.mav.command_long_send(
            self.pixhawk.target_system,
            self.pixhawk.target_component,
            command,
            0,  # confirmation
            p1, p2, p3, p4, p5, p6, p7
        )

    def move(self, motor1_speed, motor2_speed, motor3_speed, motor4_speed):
        self.set_motor_speed(1, motor1_speed)
        self.set_motor_speed(2, motor2_speed)
        self.set_motor_speed(3, motor3_speed)
        self.set_motor_speed(4, motor4_speed)

    def set_servo_pwm(self, servo_number, pwm):
        self.pixhawk.mav.command_long_send(
            self.pixhawk.target_system, self.pixhawk.target_component,
            mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
            0,
            servo_number,
            pwm,
            0, 0, 0, 0, 0
        )
        print(f"Setting servo {servo_number} to PWM: {pwm}")

    def execute_command(self, command):
        if command == "a":
            self.move(0, 0, self.motor_speed, 0)  # Yukarı
        elif command == "b":
            self.move(0, 0, -self.motor_speed, 0)  # Aşağı
        elif command == "c":
            self.move(self.motor_speed, 0, 0, 0)  # İleri
        elif command == "d":
            self.move(-self.motor_speed, 0, 0, 0)  # Geri
        elif command == "e":
            self.move(0, -self.motor_speed, 0, 0)  # Sol
        elif command == "f":
            self.move(0, self.motor_speed, 0, 0)  # Sağ
        elif command == "g":
            self.move(0, 500, 1000, 0)  # yaw
        elif command == "k":
            self.move(0, 1000, 500, 0)  # yaw
        elif command == "h":
            self.set_servo_pwm(7, 1000)  # Servo CW döndür
        elif command == "i":
            self.set_servo_pwm(7, 1500)  # Servo durdur
        elif command == "j":
            self.set_servo_pwm(7, 2000)  # Servo CCW döndür
        elif command == "n":
            print("dur")  # Tüm motorları durdur
            self.move(0, 0, 0, 0)
        elif command == "p":
            print("otonom")
            self.otonom()
        else:
            print("HATA!!!")

    def otonom(self):
        for movement in self.movements:
            if movement[0] == "wait":
                print(f"{movement[1]} saniye bekleniyor...")
                time.sleep(movement[1])
            else:
                print(f"Hareket: {movement[0]}, Süre: {movement[1]} saniye")
                self.execute_command(movement[0])
                time.sleep(movement[1])
        self.execute_command("n")  # Otonom mod sonunda dur

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