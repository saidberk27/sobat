from pymavlink import mavutil
import time
import sys

class ManualControl:
    def __init__(self, pixhawk_port='/dev/ttyACM0', motor_hiz=750):
        try:
            self.pixhawk_port = pixhawk_port
            self.motor_hiz = motor_hiz
            self.master = mavutil.mavlink_connection(pixhawk_port, baud=115200)
        except Exception as e:
            print("Port Kapali")

    def getHeartBeat(self):
        try:
            self.master.wait_heartbeat()
            print("Kalp Atisi")
        except Exception as e:
            print("Port Kapali")
    
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
            print("Port Kapali")
    
    def move(self, x, y, z, r, duration):
        start_time = time.time()
        while time.time() - start_time < duration:
            self.master.mav.manual_control_send(
                self.master.target_system,
                x, y, z, r, 0
            )
            print(f"Hareket: x={x}, y={y}, z={z}, r={r}")
            time.sleep(0.1)  # Short delay to prevent flooding

    def thrustMotors(self):
        try:
            # Forward
            print("Ileri gidiliyor...")
            self.move(self.motor_hiz, 0, 0, 0, 3)
            
            # Backward
            print("Geri gidiliyor...")
            self.move(-self.motor_hiz, 0, 0, 0, 3)
            
            # Right
            print("Saga gidiliyor...")
            self.move(0, self.motor_hiz, 0, 0, 3)
            
            # Left
            print("Sola gidiliyor...")
            self.move(0, -self.motor_hiz, 0, 0, 3)
            
            print("Hareket tamamlandi.")
        except KeyboardInterrupt:
            print("KeyboardInterrupt: Manual control durduruldu.")
        except Exception as e:
            print(f"Hata: {e}")
        finally:
            self.master.close()
            print("Baglanti kapatildi.")

if __name__ == "__main__":
    manualControl = ManualControl(pixhawk_port='/dev/ttyACM0', motor_hiz=750)
    manualControl.getHeartBeat()
    manualControl.armPixHawk()
    manualControl.thrustMotors()
