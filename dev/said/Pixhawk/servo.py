from pymavlink import mavutil
import time

# Pixhawk'a bağlanmak için seri portu belirtin (örneğin, '/dev/ttyACM0' veya '/dev/ttyUSB0')
pixhawk_port = '/dev/ttyACM0' #ttyACM0 miniusb bağlantısı için

# MAVLink bağlantısı oluşturun
master = mavutil.mavlink_connection(pixhawk_port, baud=115200)
print("PixHawk Bağlandı!")
# ESC'yi kontrol etmek için fonksiyon
def control_esc(channel, pwm_value):
    print("Komut Gönderildi")
    msg = master.mav.command_long_encode(
        1,                                      # Sistem ID
        1,                                      # Bileşen ID
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO,   # Komut
        0,                                      # İç zaman damgası (mikrosaniye)
        channel,                                # Kanal numarası (ESC'ye bağlı PWM kanalı)
        pwm_value,                              # PWM değeri (1000-2000 arası)
        0, 0, 0, 0, 0)                          # Parametreler
    master.mav.send(msg)

if __name__ == "__main__":
    try:
        channel = 1 
        for i in range(1500, 2000, 10):
            pwm_value = i
            control_esc(channel, pwm_value)
        
            time.sleep(0.1)
            print(pwm_value)
    except KeyboardInterrupt:
        pass
