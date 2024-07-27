import serial
from pymavlink import mavutil
import time


class SubmarineControl:
    def __init__(self, pixhawk_port='/dev/ttyACM0', bluetooth_port='/dev/ttyUSB0'):
        self.pixhawk = mavutil.mavlink_connection(pixhawk_port, baud=115200)
        self.bluetooth = serial.Serial(bluetooth_port, 9600, timeout=1)
        self.last_command = None
        self.movements = [('wait', 7.0), ('forward', 3.0), ('right', 5.0), ('left', 2.0), ('up', 5.0), ('down', 2.0)]
        self.mode = 'STABILIZE'

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

    def set_mode(self, mode):
        if mode not in ['MANUAL', 'STABILIZE']:
            print("Invalid mode. Choose 'MANUAL' or 'STABILIZE'")
            return

        mode_id = self.pixhawk.mode_mapping()[mode]
        self.pixhawk.mav.set_mode_send(
            self.pixhawk.target_system,
            mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
            mode_id)

        while True:
            msg = self.pixhawk.recv_match(type='HEARTBEAT', blocking=True)
            if msg.custom_mode == mode_id:
                print(f"Mode changed to {mode}")
                self.mode = mode
                break

    def set_motor_speed(self, motor_number, speed_percent):
        pwm = 1100 + (speed_percent / 100.0) * 800
        pwm = int(pwm)

        self.pixhawk.mav.command_long_send(
            self.pixhawk.target_system, self.pixhawk.target_component,
            mavutil.mavlink.MAV_CMD_DO_MOTOR_TEST,
            0, motor_number, mavutil.mavlink.MOTOR_TEST_THROTTLE_PERCENT,
            speed_percent, 0, 0, 0, 0)
        print(f"Setting motor {motor_number} to {speed_percent}% speed (PWM: {pwm})")

    def move_manual(self, motor1_speed, motor2_speed, motor3_speed, motor4_speed):
        self.set_motor_speed(1, motor1_speed)
        self.set_motor_speed(2, motor2_speed)
        self.set_motor_speed(3, motor3_speed)
        self.set_motor_speed(4, motor4_speed)

    def move_stabilize(self, roll, pitch, yaw, throttle):
        # Convert -100 to 100 range to RC PWM range (typically 1000-2000)
        roll_pwm = 1500 + (roll / 100.0) * 500
        pitch_pwm = 1500 + (pitch / 100.0) * 500
        yaw_pwm = 1500 + (yaw / 100.0) * 500
        throttle_pwm = 1000 + (throttle / 100.0) * 1000

        self.pixhawk.mav.rc_channels_override_send(
            self.pixhawk.target_system, self.pixhawk.target_component,
            int(roll_pwm), int(pitch_pwm), int(throttle_pwm), int(yaw_pwm),
            0, 0, 0, 0)

    def execute_command(self, command):
        if self.mode == 'MANUAL':
            if command == "forward":
                self.move_manual(70, 70, 0, 0)
            elif command == "backward":
                self.move_manual(-70, -70, 0, 0)
            elif command == "right":
                self.move_manual(70, -70, 0, 0)
            elif command == "left":
                self.move_manual(-70, 70, 0, 0)
            elif command == "up":
                self.move_manual(0, 0, 70, 70)
            elif command == "down":
                self.move_manual(0, 0, -70, -70)
            elif command == "stop":
                self.move_manual(0, 0, 0, 0)
            elif command == "stabilize":
                self.set_mode('STABILIZE')
            else:
                print("Geçersiz komut!")
        elif self.mode == 'STABILIZE':
            if command == "forward":
                self.move_stabilize(0, 50, 0, 50)
            elif command == "backward":
                self.move_stabilize(0, -50, 0, 50)
            elif command == "right":
                self.move_stabilize(50, 0, 0, 50)
            elif command == "left":
                self.move_stabilize(-50, 0, 0, 50)
            elif command == "up":
                self.move_stabilize(0, 0, 0, 70)
            elif command == "down":
                self.move_stabilize(0, 0, 0, 30)
            elif command == "stop":
                self.move_stabilize(0, 0, 0, 0)
            elif command == "manual":
                self.set_mode('MANUAL')
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