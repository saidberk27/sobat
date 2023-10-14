#include "Sobat.h"

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
  _trigPin = trigPin;  // M1 değerini özel özelliğe (_M1) atama
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
