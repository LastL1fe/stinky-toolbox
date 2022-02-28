#include <Servo.h>
#include <LiquidCrystal.h>

int photoPin = A1;
const int squirtPin = 2;

String coords;

bool boolVal;
bool OWfire = false;

Servo leftX;
Servo leftY;
Servo rightX;
Servo rightY;

LiquidCrystal lcd(8, 9, 10, 11, 12, 13);

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(15);

  leftX.attach(3);
  leftY.attach(4);
  rightX.attach(5);
  rightY.attach(6);

  rightY.write(63);

  pinMode(squirtPin, OUTPUT);
  digitalWrite(squirtPin, HIGH);
  
  lcd.begin(16, 2);
  lcd.write("waiting for coords");
}

void loop() {
  photoLight();
  Serial.flush();
}

void serialEvent(){
  if (not OWfire or not boolVal){
    while (Serial.available() > 0){
      
       coords = "";
       coords = Serial.readStringUntil('\0');
       
       lcdDisplayStuff();
       
       leftX.write(parseX1(coords));
       leftY.write(parseY1(coords));
       rightX.write(parseX2(coords));
       rightY.write(parseY2(coords));

       parseBool(coords);
       
       if (boolVal){
        Serial.end();
        digitalWrite(squirtPin, LOW);
        lcd.clear();
        lcd.write("eat shit");
        delay(5000);
        digitalWrite(squirtPin, HIGH); 
        boolVal = false;
        lcd.clear();
        lcd.write("resetting");
        delay(3000);
        resetPos();
        Serial.begin(9600);
       }
    }
  }
}

void photoLight(){
  int photoVal = analogRead(photoPin);
  if (photoVal > 120){overrideMain();}
}

void overrideMain(){
  if (not boolVal){
    OWfire = true;
    lcd.clear();
    lcd.write("eat shit bitch");
    leftX.write(120);
    rightX.write(60);
    digitalWrite(squirtPin, LOW);
    delay(3000);
    digitalWrite(squirtPin, HIGH);
    delay(3000);
    OWfire = false;
    resetPos();
  }
}

void lcdDisplayStuff(){
    lcd.clear();
    lcd.print(coords);
}

void parseBool(String coordsparse){
 coordsparse.remove(0, coordsparse.indexOf("/") + 1);
 if (coordsparse == "1"){boolVal = true;}
 else{boolVal = false;}
}

void resetPos(){
  lcd.clear();
  lcd.write("waiting for coords");
  leftX.write(90);
  rightX.write(90);
  leftY.write(90);
  rightY.write(90);
}

int parseX1(String coords){
  coords.remove(coords.indexOf(":"));
  return coords.toInt();
}

int parseY1(String coords){
  coords.remove(0, coords.indexOf(":") + 1);
  coords.remove(coords.indexOf(","));
  return coords.toInt();
}

int parseX2(String coords){
  coords.remove(0, coords.indexOf(",") + 1);
  coords.remove(coords.indexOf(":"));
  return coords.toInt();
}

int parseY2(String coords){
  coords.remove(0, coords.indexOf(","));
  coords.remove(coords.indexOf(","), coords.indexOf(":") + 1);
  return coords.toInt();
}
