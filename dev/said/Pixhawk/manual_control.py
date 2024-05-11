from pymavlink import mavutil
import time
import sys

class ManualControl:
    def __init__(self, pixhawk_port='', motor_hiz=0):
        try:
            self.pixhawk_port = pixhawk_port
            self.motor_hiz = motor_hiz
            self.master = mavutil.mavlink_connection(pixhawk_port, baud=115200)
        
        except Exception as e:
            print("Port Kapalı")

    def getHeartBeat(self):
        try:
            self.master.wait_heartbeat()
            print("Kalp Atışı")
        except Exception as e:
            print("Port Kapalı")
    
    def armPixHawk(self):
        try:
            #ARM
            self.master.mav.command_long_send(
                self.master.target_system,
                self.master.target_component,
                mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
                0,
                1, 0, 0, 0, 0, 0, 0)

            print("Waiting for the vehicle to arm")
            self.master.motors_armed_wait()
            print('Armed!')
            
        except Exception as e:
            print("Port Kapalı")
    
    def thrustMotors(self):
        i = 0
    
        try:
            self.master.mav.manual_control_send(
                self.master.target_system,
                self.motor_hiz,   
                0,     
                0,      
                0,      
                0      
            )
            print("Veri Gönderiliyor")

            self.master.close()

        except KeyboardInterrupt:
            print("KeyboardInterrupt: Stopping manual control.")

        except Exception:
            print("Port Kapalı")


if __name__ == "__main__":
    manualControl = ManualControl(pixhawk_port='/dev/ttyACM0', motor_hiz=750)
    manualControl.getHeartBeat()
    manualControl.armPixHawk()
    manualControl.thrustMotors()
