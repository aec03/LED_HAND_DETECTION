#include <LiquidCrystal.h>
#include <BigNumbers.h>

// LCD Pins
const int rs = 13;
const int en = 12;
const int d4 = 11;
const int d5 = 10;
const int d6 = 9;
const int d7 = 8;

// initialize LCD object
LiquidCrystal LCD(rs, en, d4, d5, d6, d7);
BigNumbers bigNum(&LCD);

int numb;

void setup() {
  Serial.begin(115200);
  LCD.begin(16, 2);
  bigNum.begin();

  delay(500);
}

void loop() {
  num = readData();
}

int readData() {
  while (Serial.available() == 0) {};
  int number = Serial.read();
  number = number - '0';
  return number;
}


//  
