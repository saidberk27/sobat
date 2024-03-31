import matplotlib.pyplot as plt
from pymavlink import mavutil
import time

# Bağlantı parametrelerini ayarla
connection_string = '/dev/ttyUSB0'  # Bağlantınıza uygun olarak değiştirin (örneğin, USB, seri, vb.)
baud_rate = 115200  # Gerekirse baud oranını güncelleyin

# Pixhawk'a bağlan
master = mavutil.mavlink_connection(connection_string, baud=baud_rate)
print("Bağlandı")
# Pixhawk'tan kalp atışını bekleyin
while True:
    msg = master.recv_match(type='HEARTBEAT', blocking=True)
    if msg:
        print('Pixhawk bağlandı!')
        break
    time.sleep(1)

# Dijital jiroskop verilerini iste
master.mav.request_data_stream_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_DATA_STREAM_RAW_SENSORS,
    10,  # Hz cinsinden hız (gerektiğinde ayarlayın)
    1  # Göndermeye başla
)

# Veri depolama için listeleri tanımla
gyro_x_data = []
gyro_y_data = []
gyro_z_data = []

# Matplotlib figürünü oluştur
fig, ax = plt.subplots()

# Ana döngü
try:
    while True:
        msg = master.recv_match(type='RAW_IMU', blocking=True)
        if msg:
            # Jiroskop verilerini depola
            gyro_x_data.append(msg.xgyro)
            gyro_y_data.append(msg.ygyro)
            gyro_z_data.append(msg.zgyro)

            # Veriyi güncelle ve çizimi yeniden çiz
            ax.clear()
            ax.plot(gyro_x_data, label='Gyro X')
            ax.plot(gyro_y_data, label='Gyro Y')
            ax.plot(gyro_z_data, label='Gyro Z')
            ax.set_title('Gyro Data')
            ax.set_xlabel('Time')
            ax.set_ylabel('Angular Velocity')
            ax.legend()
            plt.pause(0.01)  # Çizimi güncelleme aralığı (saniye cinsinden)

except KeyboardInterrupt:
    pass
finally:
    master.close()
