import serial

# Seri iletişim bağlantısını açın (COMx, ttyUSB0 gibi bir bağlantı noktasını belirtin)
ser = serial.Serial('COM8', 9600)  # Arduino'nun bağlantı hızına uygun hızı ayarlayın

while True:
    # Arduino'dan gelen veriyi okuma
    received_data = ser.readline()

    # Veriyi işleme veya ekrana yazdırma
    distance = received_data.decode('utf-8')  # Veriyi metinden sayıya dönüştürün
    print(distance)

# Seri iletişim bağlantısını kapatın
ser.close()
