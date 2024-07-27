from pymavlink import mavutil
import time
import sys
import select


class MotorControl:
    def __init__(self, pixhawk_port='/dev/ttyACM0', motor_speed=750):
        try:
            self.pixhawk_port = pixhawk_port
            self.motor_speed = motor_speed
            self.master = mavutil.mavlink_connection(pixhawk_port, baud=115200)
            self.movements = []
        except Exception as e:
            print("Bağlantı Hatası:", e)

    def get_heartbeat(self):
        try:
            self.master.wait_heartbeat()
            print("Kalp Atışı Alındı")
        except Exception as e:
            print("Port Kapalı:", e)

    def arm_vehicle(self):
        self.master.arducopter_arm()
        self.master.motors_armed_wait()
        print("Vehicle armed")

    def set_mode(self, mode):
        if mode not in self.master.mode_mapping():
            print('Unknown mode : {}'.format(mode))
            print('Try:', list(self.master.mode_mapping().keys()))
            return False

        mode_id = self.master.mode_mapping()[mode]
        self.master.set_mode(mode_id)

        ack = False
        while not ack:
            ack_msg = self.master.recv_match(type='COMMAND_ACK', blocking=True)
            ack_msg = ack_msg.to_dict()
            if ack_msg['command'] == mavutil.mavlink.MAV_CMD_DO_SET_MODE:
                ack = True
                print(mavutil.mavlink.enums['MAV_RESULT'][ack_msg['result']].description)
                break
        return True

    def get_current_mode(self):
        while True:
            msg = self.master.recv_match(type='HEARTBEAT', blocking=True)
            if msg:
                mode = mavutil.mode_string_v10(msg)
                print(f"Current mode: {mode}")
                return mode

    def move(self, x, y, z, r, duration):
        start_time = time.time()
        while time.time() - start_time < duration:
            self.master.mav.manual_control_send(
                self.master.target_system,
                x, y, z, r, 0
            )
            print(f"Hareket: x={x}, y={y}, z={z}, r={r}")
            time.sleep(0.1)

            if self.check_for_stop():
                return True
        return False

    def check_for_stop(self):
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            key = sys.stdin.read(1)
            if key.lower() == 'q':
                print("Q tuşuna basıldı. Motorlar durduruluyor.")
                self.stop_motors()
                return True
        return False

    def stop_motors(self):
        # Tüm motorlara 3000 hız gönder
        self.master.mav.manual_control_send(
            self.master.target_system,
            3000, 3000, 3000, 3000, 3000)

        print("Motors stopped with 3000 speed")

        # Aracı disarm et
        self.master.mav.command_long_send(
            self.master.target_system,
            self.master.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0,
            0, 0, 0, 0, 0, 0, 0)

        print("Vehicle disarmed")

        for _ in range(10):
            if not self.master.motors_armed():
                print("Disarm confirmed")
                break
            time.sleep(0.1)
        else:
            print("WARNING: Disarm could not be confirmed")

    def get_user_input(self):
        initial_wait = float(input("Başlangıç bekleme süresi (saniye): "))
        self.movements.append(("wait", initial_wait))

        while True:
            print("\nHareket Yönü:")
            print("1 - İleri")
            print("2 - Geri")
            print("3 - Sağ")
            print("4 - Sol")
            print("5 - Yukarı")
            print("6 - Aşağı")
            print("Q - Çıkış ve Hareketleri Başlat")

            choice = input("Seçiminiz: ").lower()

            if choice == 'q':
                break

            if choice not in ['1', '2', '3', '4', '5', '6']:
                print("Geçersiz seçim. Lütfen tekrar deneyin.")
                continue

            duration = float(input("Hareket süresi (saniye): "))
            self.movements.append((choice, duration))

    def execute_movements(self):
        try:
            for movement in self.movements:
                if movement[0] == "wait":
                    print(f"{movement[1]} saniye bekleniyor...")
                    time.sleep(movement[1])
                    if self.check_for_stop():
                        break
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
                    if self.move(x, y, z, r, movement[1]):
                        break
        finally:
            self.stop_motors()
            print("All movements completed. Motors stopped.")

    def run(self):
        self.get_heartbeat()
        self.arm_vehicle()
        if self.set_mode('STABILIZE'):
            current_mode = self.get_current_mode()
            if current_mode == 'STABILIZE':
                print("Mode successfully changed to Stabilize")
                self.get_user_input()
                self.execute_movements()
                print("Tüm hareketler tamamlandı.")
            else:
                print("Failed to change mode to Stabilize")
        else:
            print("Failed to set mode to Stabilize")


if __name__ == "__main__":
    motor_control = MotorControl(pixhawk_port='/dev/ttyACM0', motor_speed=750)
    motor_control.run()