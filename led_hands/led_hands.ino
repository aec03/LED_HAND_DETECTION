/* OPENCV x ARDUINO HAND CONTROLLED LEDs */

// LED pins
const int LED1 = 8;
const int LED2 = 9;
const int LED3 = 10;
const int LED4 = 11;
const int LED5 = 12;

// delay time
const int dt = 0;

void setup() {
  Serial.begin(115200);

  // pin modes
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  pinMode(LED4, OUTPUT);
  pinMode(LED5, OUTPUT);

  // delay start
  delay(500);
}

void loop() {
  int num = readData();
  triggerLEDs(num);

  delay(dt);
}

int readData() {
  // wait for serial monitor to turn on
  while (Serial.available() == 0) {};

  // read serial monitor as char
  int number = Serial.read();

  // convert char to int
  number = number - '0';
  
  return number;
}

void triggerLEDs(int num) {
  // turn all pins off
  digitalWrite(LED1, LOW);;
  digitalWrite(LED2, LOW);
  digitalWrite(LED3, LOW);
  digitalWrite(LED4, LOW);
  digitalWrite(LED5, LOW);
  
  if (num - 1 >= 0) {
    digitalWrite(LED1, HIGH);
    num -= 1;
  }
  if (num - 1 >= 0) {
    digitalWrite(LED2, HIGH);
    num -= 1;
  }
  if (num - 1 >= 0) {
    digitalWrite(LED3, HIGH);
    num -= 1;
  }
  if (num - 1 >= 0) {
    digitalWrite(LED4, HIGH);
    num -= 1;
  }
  if (num - 1 >= 0) {
    digitalWrite(LED5, HIGH);
    num -= 1;
  }
  
}
