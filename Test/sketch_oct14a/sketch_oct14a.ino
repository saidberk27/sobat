#include <sobat.h>

int M1 = 1;
int M2 = 2;
int M3 = 3;
int M4 = 4;
int M5 = 5;
int M6 = 6;

int L1 = 7;
int L2 = 8;

int servoPin = 9;
int echoPin = 10;
int trigPin = 11;

Sobat sobat(M1, M2, M3, M4, M5, M6, L1, L2, servoPin, echoPin, trigPin); // M1 değerini 42 olarak ayarla

void setup() {
  Serial.begin(9600);
  sobat.getPinInfo();
  sobat.setup();
}
void loop() {
   sobat.moveForward();
   delay(3000);
   sobat.stop();
   delay(1000000);
}
