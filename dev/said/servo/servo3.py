import serial
import time

# Arduino'nun bağlı olduğu seri portu belirtin
# Windows'ta genellikle 'COM3' gibi bir port adı olur
# Linux veya macOS'ta '/dev/ttyUSB0' veya '/dev/ttyACM0' gibi bir port adı olur
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
time.sleep(2)  # Arduino'nun yeniden başlaması için bekle

def set_servo_angle(angle):
    ser.write(str(angle).encode())
    time.sleep(0.1)  # Servo'nun hareket etmesi için kısa bir bekleme
    response = ser.readline().decode().strip()
    print(response)

try:
    while True:
        # Servo'yu 0 ile 180 derece arasında hareket ettir
        set_servo_angle(90)
        print("Atış yok")
        time.sleep(2)
        print("Atış serbest")
        set_servo_angle(180)
        time.sleep(0.2)


except KeyboardInterrupt:
    print("Program sonlandırıldı.")
    ser.close()
