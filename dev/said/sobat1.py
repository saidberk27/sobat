import time
from pymavlink import mavutil

class SubmarineControl:
    def __init__(self, pixhawk_port='/dev/ttyACM0'):
        self.pixhawk = mavutil.mavlink_connection(pixhawk_port, baud=115200)
        self.motor_speed = 1500
        self.last_command = None
        self.movements = [('wait', 7.0), ('s', 3.0), ('e', 5.0), ('q', 2.0), ('w', 5.0), ('d', 2.0), ('a', 3.0), ('w', 10.0)]
        self.is_programmed_movement = False

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

    def read_user_input(self):
        try:
            while True:
                command = input("Enter command (w/a/s/d/q/e/r/f/z/x/c/v/b/n/p): ").lower().strip()
                if command:
                    print(f"Received command: {command}")
                    self.check_arm_status()
                    self.execute_command(command)
                    self.last_command = command
                elif self.last_command:
                    print(f"Re-sending last command: {self.last_command}")
                    self.check_arm_status()
                    self.execute_command(self.last_command)
        except KeyboardInterrupt:
            print("Program stopped.")

    def move_duration(self, x, y, z, r, duration):
        start_time = time.time()
        while time.time() - start_time < duration:
            self.pixhawk.mav.manual_control_send(
                self.pixhawk.target_system,
                x, y, z, r, 0
            )
            print(f"Movement: x={x}, y={y}, z={z}, r={r}")
            time.sleep(0.1)
        return False

    def set_servo_pwm(self, servo_number, pwm_value):
        self.pixhawk.mav.command_long_send(
            self.pixhawk.target_system, self.pixhawk.target_component,
            mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
            0, servo_number, pwm_value, 0, 0, 0, 0, 0
        )
        print(f"Setting servo {servo_number} to PWM {pwm_value}")

    def move(self, x, y, z, r):
        self.pixhawk.mav.manual_control_send(
            self.pixhawk.target_system,
            x, y, z, r, 0
        )

    def otonom(self):
        for movement in self.movements:
            if movement[0] == "wait":
                print(f"Waiting for {movement[1]} seconds...")
                time.sleep(movement[1])
            else:
                x, y, z, r = 0, 0, 0, 0
                if movement[0] == 'w':  # Forward
                    x = self.motor_speed
                elif movement[0] == 's':  # Backward
                    x = -self.motor_speed
                elif movement[0] == 'd':  # Right
                    y = self.motor_speed
                elif movement[0] == 'a':  # Left
                    y = -self.motor_speed
                elif movement[0] == 'r':  # Up
                    z = self.motor_speed
                elif movement[0] == 'f':  # Down
                    z = -self.motor_speed
                elif movement[0] == 'q':  # Rotate left
                    r = -self.motor_speed
                elif movement[0] == 'e':  # Rotate right
                    r = self.motor_speed

                print(f"Movement direction: {movement[0]}, Duration: {movement[1]} seconds")
                if self.move_duration(x, y, z, r, movement[1]):
                    break

    def execute_command(self, command):
        if command == "r":
            self.move(0, 0, self.motor_speed, 0)  # Up
        elif command == "f":
            self.move(0, 0, -self.motor_speed, 0)  # Down
        elif command == "w":
            self.move(self.motor_speed, 0, 0, 0)  # Forward
        elif command == "s":
            self.move(-self.motor_speed, 0, 0, 0)  # Backward
        elif command == "a":
            self.move(0, -self.motor_speed, 0, 0)  # Left
        elif command == "d":
            self.move(0, self.motor_speed, 0, 0)  # Right
        elif command == "q":
            self.move(0, 0, 0, -self.motor_speed)  # Rotate left
        elif command == "e":
            self.move(0, 0, 0, self.motor_speed)  # Rotate right
        elif command == "z":
            self.set_servo_pwm(7, 1000)  # Servo CW rotate
        elif command == "x":
            self.set_servo_pwm(7, 1500)  # Servo stop
        elif command == "c":
            self.set_servo_pwm(7, 2000)  # Servo CCW rotate
        elif command == "v":
            print("Stop")  # Stop all motors
        elif command == "p":
            print("Autonomous mode")
            self.otonom()
        else:
            print("ERROR: Invalid command")

    def run(self):
        try:
            self.pixhawk.wait_heartbeat()
            self.arm_vehicle()
            print("*** Vehicle armed")
            self.read_user_input()
        except KeyboardInterrupt:
            print("Program interrupted by user")
        finally:
            print("Vehicle disarmed")
            self.pixhawk.arducopter_disarm()
            self.pixhawk.motors_disarmed_wait()

if __name__ == "__main__":
    submarine = SubmarineControl()
    submarine.run()