#include "Sobat.h"
#include <Servo.h>

Servo esc1; // 1. motorun ESC'si
Servo esc2; // 2. motorun ESC'si
Servo esc3; // 3. motorun ESC'si
Servo esc4; // 4. motorun ESC'si
Servo esc5; // 5. Motorun ESC’si
Servo esc6; // 6. Motorun ESC’si


Sobat::Sobat(
  int M1,
  int M2,
  int M3,
  int M4,
  int M5,
  int M6,

  int L1,
  int L2,

  int servoPin,
  int echoPin,
  int trigPin

) {
  _M1 = M1;
  _M2 = M2;
  _M3 = M3;
  _M4 = M4;
  _M5 = M5;
  _M6 = M6;
  _L1 = L1;
  _L2 = L2;
  _servoPin = servoPin;
  _echoPin = echoPin;
  _trigPin = trigPin;

}

void Sobat::setup(){
  Serial.println("Setup");
  esc1.attach(6);
  esc2.attach(9);
  esc3.attach(10);
  esc4.attach(11);

  delay(3500);
  esc1.writeMicroseconds(1500);
  delay(100);
  esc1.writeMicroseconds(2000);

}

void Sobat::moveForward(){
    Serial.println("Moving Forward...");
      for(int speed = 1941; speed <= 1950; speed = speed + 10){

          esc1.writeMicroseconds(speed);
          esc2.writeMicroseconds(speed);
          esc3.writeMicroseconds(speed);
          esc4.writeMicroseconds(speed);
          esc5.writeMicroseconds(speed);
          esc6.writeMicroseconds(speed); 
      
          delay(100);
          Serial.println(speed);
 }
}

void Sobat::stop(){
    Serial.println("Stopping...");
        esc1.writeMicroseconds(1500);
        esc2.writeMicroseconds(1500);
        esc3.writeMicroseconds(1500);
        esc4.writeMicroseconds(1500);
        esc5.writeMicroseconds(1500);
        esc6.writeMicroseconds(1500); 
        
        delay(100);
}

void Sobat::getPinInfo() {
  Serial.print("MOTOR 1:");
  Serial.println(_M1);

  Serial.print("MOTOR 2:");
  Serial.println(_M2);

  Serial.print("MOTOR 3:");
  Serial.println(_M3);

  Serial.print("MOTOR 4:");
  Serial.println(_M4);

  Serial.print("MOTOR 5:");
  Serial.println(_M5);

  Serial.print("MOTOR 6:");
  Serial.println(_M6);


  Serial.print("LIGHT 1:");
  Serial.println(_L1);

  Serial.print("LIGHT 2:");
  Serial.println(_L2);

  Serial.print("SERVO: ");
  Serial.println(_servoPin);

  Serial.print("DISTANCE ECHO: ");
  Serial.println(_echoPin);

  Serial.print("DISTANCE TRIG: ");
  Serial.println(_trigPin);
  
}