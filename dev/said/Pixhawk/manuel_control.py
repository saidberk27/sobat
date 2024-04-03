from pymavlink import mavutil
import time
import sys
pixhawk_port = '/dev/ttyACM0' 

motor_hiz = 750 #-1000 - 0 /Saat Yönünün Tersine || 0 - 1000 Saat Yönünde
master = mavutil.mavlink_connection(pixhawk_port, baud=115200)


master.wait_heartbeat()
print("Kalp Atışı")

#ARM
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1, 0, 0, 0, 0, 0, 0)

print("Waiting for the vehicle to arm")
master.motors_armed_wait()
print('Armed!')

try:
    while True:

        master.mav.manual_control_send(
            master.target_system,
            500,   
            0,     
            0,      
            0,      
            0      
        )
        print("Veri Gönderiliyor")

       
        time.sleep(0.1)  

except KeyboardInterrupt:
    print("KeyboardInterrupt: Stopping manual control.")


master.close()