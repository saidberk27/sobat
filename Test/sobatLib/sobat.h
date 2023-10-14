#ifndef Sobat_h
#define Sobat_h

#include <Arduino.h>

class Sobat {
public:
  Sobat(
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
  );  // Kurucu fonksiyon
  void getPinInfo();  // Örnek işlev

private:
  int _M1;
  int _M2;
  int _M3;
  int _M4;
  int _M5;
  int _M6;

  int _L1;
  int _L2;

  int _servoPin;

  int _echoPin;
  int _trigPin;
};

#endif
