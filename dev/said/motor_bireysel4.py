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

    def set_motor_pwm(self, channel, pwm):
        logging.debug(f"Setting motor {channel} to PWM: {pwm}")
        try:
            self.pixhawk.mav.command_long_send(
                self.pixhawk.target_system, self.pixhawk.target_component,
                mavutil.mavlink.MAV_CMD_DO_MOTOR_TEST,
                0, channel, 1, pwm, 1000, 1, 0, 0
            )
            logging.info(f"Motor {channel} PWM command sent, waiting for ACK")

            ack = self.wait_for_command_ack(mavutil.mavlink.MAV_CMD_DO_MOTOR_TEST)

            if ack:
                logging.info(f"Motor {channel} PWM set to {pwm} - ACK received: {ack}")
            else:
                logging.warning(f"No ACK received for motor {channel} PWM command")
        except Exception as e:
            logging.error(f"Failed to set motor {channel} PWM: {e}")

    def wait_for_command_ack(self, command, timeout=3):
        start = time.time()
        while time.time() - start < timeout:
            msg = self.pixhawk.recv_match(type='COMMAND_ACK', blocking=True, timeout=1)
            if msg and msg.command == command:
                return msg.result
        return None

    def move(self, motor1_pwm, motor2_pwm, motor3_pwm, motor4_pwm):
        logging.info(f"Moving with PWM values: M1={motor1_pwm}, M2={motor2_pwm}, M3={motor3_pwm}, M4={motor4_pwm}")
        self.set_motor_pwm(1, motor1_pwm)
        self.set_motor_pwm(2, motor2_pwm)
        self.set_motor_pwm(3, motor3_pwm)
        self.set_motor_pwm(4, motor4_pwm)

    def execute_command(self, command):
        logging.info(f"Executing command: {command}")
        if command == "a":
            self.move(1500, 1500, 1700, 1700)  # Up
        elif command == "b":
            self.move(1500, 1500, 1300, 1300)  # Down
        elif command == "c":
            self.move(1700, 1700, 1500, 1500)  # Forward
        elif command == "d":
            self.move(1300, 1300, 1500, 1500)  # Backward
        elif command == "e":
            self.move(1300, 1700, 1500, 1500)  # Left
        elif command == "f":
            self.move(1700, 1300, 1500, 1500)  # Right
        elif command == "n":
            self.move(1500, 1500, 1500, 1500)  # Stop
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