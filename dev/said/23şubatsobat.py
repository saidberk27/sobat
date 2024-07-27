import serial
from pymavlink import mavutil
import time

class SubmarineControl:
    def __init__(self, pixhawk_port='/dev/ttyACM0', bluetooth_port='/dev/ttyUSB0', baud_rate=9600):
        self.pixhawk = mavutil.mavlink_connection(pixhawk_port, baud=115200)
        self.bluetooth = serial.Serial(bluetooth_port, baud_rate, timeout=1)
        self.motor_speed = 750
        self.last_command = None
        self.movements = [('wait', 3.0), ('1', 2.0), ('2', 2.0), ('3', 2.0), ('4', 2.0), ('5', 2.0), ('6', 2.0), ('1', 2.0), ('2', 2.0), ('3', 2.0), ('4', 2.0), ('5', 2.0), ('6', 2.0), ('1', 2.0), ('2', 2.0), ('3', 2.0), ('4', 2.0), ('5', 2.0), ('6', 2.0), ('1', 2.0), ('2', 2.0), ('3', 2.0), ('4', 2.0), ('5', 2.0), ('6', 2.0), ('1', 2.0), ('2', 2.0), ('3', 2.0), ('4', 2.0), ('5', 2.0), ('6', 2.0)]
        self.is_programmed_movement = False

    def wait_heartbeat(self):
        print("Waiting for heartbeat...")
        self.pixhawk.wait_heartbeat()
        print("Heartbeat received!")

    def arm_vehicle(self):
        self.pixhawk.arducopter_arm()
        self.pixhawk.motors_armed_wait()
        print("Vehicle armed")

    def check_arm_status(self):
        self.pixhawk.wait_heartbeat()
        if not self.pixhawk.motors_armed():
            print("Vehicle is disarmed. Re-arming...")
            self.arm_vehicle()
        else:
            print("Vehicle is armed")

    def read_bluetooth_data(self):
        try:
            while True:
                if self.is_programmed_movement:
                    continue  # Programlanmış hareket devam ediyorsa, Bluetooth komutlarını işleme

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

    def execute_command(self, command):
        if command == "c":
            self.move(self.motor_speed, 0, 0, 0)  # Forward
        elif command == "d":
            self.move(-self.motor_speed, 0, 0, 0)  # Backward
        elif command == "e":
            self.move(0, -self.motor_speed, 0, 0)  # Left
        elif command == "f":
            self.move(0, self.motor_speed, 0, 0)  # Right
        elif command == "a":
            self.move(0, 0, self.motor_speed, 0)  # Up
        elif command == "b":
            self.move(0, 0, -self.motor_speed, 0)  # Down
        elif command == "i":
            self.set_servo_pwm(7, 1500)  # Servo 0 degrees            
        elif command == "g":
            print("dur")  # Servo 135 degrees
        elif command == "h":
            self.set_servo_pwm(7, 1000)  # Servo 45 degrees
        elif command == "n":
            self.move(0, 0, 0, 0)  # No movement (Yeni eklenen)
        elif command == "p":
            self.is_programmed_movement = True  # Programlanmış hareketi başlat (Yeni eklenen)
            self.execute_programmed_movements()
        else:
            self.move(0, 0, 0, 0)  # No movement

    def execute_programmed_movements(self):
        for movement in self.movements:
            if not self.is_programmed_movement:
                break
            if movement[0] == "wait":
                print(f"{movement[1]} saniye bekleniyor...")
                time.sleep(movement[1])
            else:
                x, y, z, r = 0, 0, 0, 0
                if movement[0] == '1':  # İleri
                    x = self.motor_speed
                elif movement[0] == '2':  # Geri
                    x = -self.motor_speed
                elif movement[0] == '3':  # Sağ
                    y = self.motor_speed
                elif movement[0] == '4':  # Sol
                    y = -self.motor_speed
                elif movement[0] == '5':  # Yukarı
                    z = self.motor_speed
                elif movement[0] == '6':  # Aşağı
                    z = -self.motor_speed

                print(f"Hareket yönü: {movement[0]}, Süre: {movement[1]} saniye")
                self.move(x, y, z, r)
                time.sleep(movement[1])

        self.is_programmed_movement = False
        print("Programlanmış hareketler tamamlandı.")

    def run(self):
        try:
            self.wait_heartbeat()
            self.arm_vehicle()
            print("***1 arm edildi")
            self.read_bluetooth_data()
            print("***bluetooth verisi alınamadı")
        except KeyboardInterrupt:
            print("Program interrupted by user")
        finally:
            print("Vehicle disarmed")
            self.pixhawk.arducopter_disarm()

if __name__ == "__main__":
    submarine = SubmarineControl()
    submarine.run()