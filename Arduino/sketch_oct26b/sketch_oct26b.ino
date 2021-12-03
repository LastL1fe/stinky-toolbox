//throw away code

#include <LiquidCrystal.h>
#include <Servo.h>

String serialShit;
String serialDisplay;

Servo x1;
Servo y1;
Servo x2;
Servo y2;

LiquidCrystal screen(13, 12, 11, 10, 9, 8);

void setup() {
  x1.attach(3);
  y1.attach(4);
  x2.attach(5);
  y2.attach(6);

  Serial.begin(9600);
  Serial.setTimeout(60);

  screen.begin(16, 2);
}

void loop() {
  delay(100);
  while (Serial.available()){
    if (Serial.available() > 0){
      serialDisplay = Serial.read();
      screen.write(Serial.read());
    }
  }
  serialShit = Serial.readString();
}
