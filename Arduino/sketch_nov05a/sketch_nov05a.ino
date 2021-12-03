//throw away code

#include <Servo.h>

Servo test;
Servo test2;

void setup() {
  pinMode(2, OUTPUT);
  digitalWrite(2, HIGH);

  test.attach(3);
  test2.attach(5);
}

void loop() {
  
}
