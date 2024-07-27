import serial
from pymavlink import mavutil
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class SubmarineControl:
    def __init__(self, pixhawk_port='/dev/ttyACM0', bluetooth_port='/dev/ttyUSB0'):
        logging.info(
            f"Initializing SubmarineControl with Pixhawk port: {pixhawk_port} and Bluetooth port: {bluetooth_port}")
        try:
            self.pixhawk = mavutil.mavlink_connection(pixhawk_port, baud=115200)
            logging.info("Pixhawk connection established")
        except Exception as e:
            logging.error(f"Failed to connect to Pixhawk: {e}")
            raise

        try:
            self.bluetooth = serial.Serial(bluetooth_port, 9600, timeout=1)
            logging.info("Bluetooth connection established")
        except Exception as e:
            logging.error(f"Failed to connect to Bluetooth: {e}")
            raise

        self.last_command = None
        self.movements = [('wait', 7.0), ('c', 3.0), ('f', 5.0), ('e', 2.0), ('a', 5.0), ('b', 2.0)]

    def arm_vehicle(self):
        logging.info("Attempting to arm vehicle")
        self.pixhawk.arducopter_arm()
        logging.info("Arm command sent, waiting for confirmation")
        self.pixhawk.motors_armed_wait()
        if self.pixhawk.motors_armed():
            logging.info("Vehicle armed successfully")
        else:
            logging.error("Failed to arm vehicle")

    def check_arm_status(self):
        logging.debug("Checking arm status")
        self.pixhawk.wait_heartbeat()
        if not self.pixhawk.motors_armed():
            logging.warning("Vehicle is disarmed. Re-arming...")
            self.arm_vehicle()
        else:
            logging.info("Vehicle is armed")

    def set_motor_speed(self, motor_number, speed_percent):
        pwm = 1100 + (speed_percent / 100.0) * 800
        pwm = int(pwm)
        logging.debug(f"Setting motor {motor_number} to {speed_percent}% speed (PWM: {pwm})")

        try:
            self.pixhawk.mav.command_long_send(
                self.pixhawk.target_system, self.pixhawk.target_component,
                mavutil.mavlink.MAV_CMD_DO_MOTOR_TEST,
                0, motor_number, mavutil.mavlink.MOTOR_TEST_THROTTLE_PERCENT,
                speed_percent, 0, 0, 0, 0
            )
            logging.info(f"Motor {motor_number} speed command sent, waiting for ACK")

            # Wait for the command acknowledgement
            ack = self.wait_for_command_ack(mavutil.mavlink.MAV_CMD_DO_MOTOR_TEST)

            if ack:
                logging.info(f"Motor {motor_number} speed set to {speed_percent}% - ACK received: {ack}")
            else:
                logging.warning(f"No ACK received for motor {motor_number} speed command")
        except Exception as e:
            logging.error(f"Failed to set motor {motor_number} speed: {e}")

    def wait_for_command_ack(self, command, timeout=3):
        start = time.time()
        while time.time() - start < timeout:
            msg = self.pixhawk.recv_match(type='COMMAND_ACK', blocking=True, timeout=1)
            if msg and msg.command == command:
                return msg.result
        return None

    def move(self, motor1_speed, motor2_speed, motor3_speed, motor4_speed):
        logging.info(f"Moving with speeds: M1={motor1_speed}, M2={motor2_speed}, M3={motor3_speed}, M4={motor4_speed}")
        self.set_motor_speed(1, motor1_speed)
        self.set_motor_speed(2, motor2_speed)
        self.set_motor_speed(3, motor3_speed)
        self.set_motor_speed(4, motor4_speed)

    def execute_command(self, command):
        logging.info(f"Executing command: {command}")
        if command == "a":
            self.move(0, 0, 70, 70)  # Up
        elif command == "b":
            self.move(0, 0, -70, -70)  # Down
        elif command == "c":
            self.move(70, 70, 0, 0)  # Forward
        elif command == "d":
            self.move(-70, -70, 0, 0)  # Backward
        elif command == "e":
            self.move(-70, 70, 0, 0)  # Left
        elif command == "f":
            self.move(70, -70, 0, 0)  # Right
        elif command == "n":
            self.move(0, 0, 0, 0)  # Stop
        else:
            logging.warning(f"Invalid command: {command}")

    def otonom(self):
        logging.info("Starting autonomous mode")
        for movement in self.movements:
            if movement[0] == "wait":
                logging.info(f"Waiting for {movement[1]} seconds")
                time.sleep(movement[1])
            else:
                logging.info(f"Autonomous movement: {movement[0]}, Duration: {movement[1]} seconds")
                self.execute_command(movement[0])
                time.sleep(movement[1])
        self.execute_command("n")
        logging.info("Autonomous mode completed")

    def read_bluetooth_data(self):
        logging.info("Starting to read Bluetooth data")
        try:
            while True:
                data = self.bluetooth.read(1).decode('utf-8').strip()
                if data:
                    logging.info(f"Received Bluetooth command: {data}")
                    self.check_arm_status()
                    self.execute_command(data)
                    self.last_command = data
                elif self.last_command:
                    logging.debug(f"Re-sending last command: {self.last_command}")
                    self.check_arm_status()
                    self.execute_command(self.last_command)
                time.sleep(0.01)
        except KeyboardInterrupt:
            logging.info("Program stopped by user")
        except Exception as e:
            logging.error(f"Error in reading Bluetooth data: {e}")
        finally:
            if self.bluetooth:
                self.bluetooth.close()
                logging.info("Bluetooth connection closed")

    def run(self):
        try:
            logging.info("Starting SubmarineControl")
            self.pixhawk.wait_heartbeat()
            logging.info("Heartbeat received from Pixhawk")
            self.arm_vehicle()
            self.read_bluetooth_data()
        except KeyboardInterrupt:
            logging.info("Program interrupted by user")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
        finally:
            logging.info("Disarming vehicle")
            self.pixhawk.arducopter_disarm()
            self.pixhawk.motors_disarmed_wait()
            logging.info("Vehicle disarmed")


if __name__ == "__main__":
    submarine = SubmarineControl()
    submarine.run()