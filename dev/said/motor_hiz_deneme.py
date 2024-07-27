from pymavlink import mavutil
import time
import sys

class ManualControl:
    def __init__(self, pixhawk_port='/dev/ttyACM0'):
        try:
            self.pixhawk_port = pixhawk_port
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
    
    def move(self, x, y, z, r):
        self.master.mav.manual_control_send(
            self.master.target_system,
            x, y, z, r, 0
        )
        print(f"Hareket: x={x}, y={y}, z={z}, r={r}")

    def speedTest(self):
        try:
            directions = [
                ("Ileri", lambda speed: (speed, 0, 0, 0)),
                ("Geri", lambda speed: (-speed, 0, 0, 0)),
                ("Saga", lambda speed: (0, speed, 0, 0)),
                ("Sola", lambda speed: (0, -speed, 0, 0))
            ]

            for direction, move_func in directions:
                print(f"{direction} yönünde hız testi başlıyor...")
                for speed in range(0, 3001, 100):
                    x, y, z, r = move_func(speed)
                    self.move(x, y, z, r)
                    time.sleep(1)
                print(f"{direction} yönünde hız testi tamamlandı.")
                time.sleep(2)  # Her yön değişiminde 2 saniye bekle

            print("Tüm yönlerde hız testi tamamlandı.")
        except KeyboardInterrupt:
            print("KeyboardInterrupt: Manuel kontrol durduruldu.")
        except Exception as e:
            print(f"Hata: {e}")
        finally:
            self.master.close()
            print("Bağlantı kapatıldı.")

if __name__ == "__main__":
    manualControl = ManualControl(pixhawk_port='/dev/ttyACM0')
    manualControl.getHeartBeat()
    manualControl.armPixHawk()
    manualControl.speedTest()