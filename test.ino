#include <SoftwareSerial.h>

SoftwareSerial BTSerial(2, 3);

// Define motor control pins
#define L1_RPWM 3
#define L1_LPWM 5
#define L1_R_EN 2
#define L1_L_EN 4
#define L2_RPWM 6
#define L2_LPWM 9
#define L2_R_EN 7
#define L2_L_EN 8
#define R1_RPWM 10
#define R1_LPWM 11
#define R1_R_EN 12  //13
#define R1_L_EN A4  //0
#define R2_RPWM A0
#define R2_LPWM A1
#define R2_R_EN A2  //1
#define R2_L_EN A3

void setupMotor(int rpwm, int lpwm, int speedR, int speedL) {
  analogWrite(rpwm, speedR);
  analogWrite(lpwm, speedL);
}

void stopAll() {
  setupMotor(L1_RPWM, L1_LPWM, 0, 0);
  setupMotor(L2_RPWM, L2_LPWM, 0, 0);
  setupMotor(R1_RPWM, R1_LPWM, 0, 0);
  setupMotor(R2_RPWM, R2_LPWM, 0, 0);
}

void setup() {
  // Initialize Serial (optional)
  Serial.begin(9600);

  // Set all motor pins as output
  pinMode(L1_RPWM, OUTPUT);
  pinMode(L1_LPWM, OUTPUT);
  pinMode(L2_RPWM, OUTPUT);
  pinMode(L2_LPWM, OUTPUT);
  pinMode(R1_RPWM, OUTPUT);
  pinMode(R1_LPWM, OUTPUT);
  pinMode(R2_RPWM, OUTPUT);
  pinMode(R2_LPWM, OUTPUT);

  pinMode(L1_R_EN, OUTPUT);
  pinMode(L1_L_EN, OUTPUT);
  pinMode(L2_R_EN, OUTPUT);
  pinMode(L2_L_EN, OUTPUT);
  pinMode(R1_R_EN, OUTPUT);
  pinMode(R1_L_EN, OUTPUT);
  pinMode(R2_R_EN, OUTPUT);
  pinMode(R2_L_EN, OUTPUT);

  // Enable all motor directions
  digitalWrite(L1_R_EN, HIGH);
  digitalWrite(L1_L_EN, HIGH);
  digitalWrite(L2_R_EN, HIGH);
  digitalWrite(L2_L_EN, HIGH);
  digitalWrite(R1_R_EN, HIGH);
  digitalWrite(R1_L_EN, HIGH);
  digitalWrite(R2_R_EN, HIGH);
  digitalWrite(R2_L_EN, HIGH);

  // Stop all motors at start
  stopAll();
}

void loop() {
  if (BTSerial.available()) {
    char inputvalue = BTSerial.read();
    switch (inputvalue) {
      case 'F':  // Move Forward
        setupMotor(L1_RPWM, L1_LPWM, 50, 0);
        setupMotor(L2_RPWM, L2_LPWM, 50, 0);
        setupMotor(R1_RPWM, R1_LPWM, 50, 0);
        setupMotor(R2_RPWM, R2_LPWM, 50, 0);
        //  delay(20000);
        break;

      case 'B': // Move Backward
        setupMotor(L1_RPWM, L1_LPWM, 0, 128);
        setupMotor(L2_RPWM, L2_LPWM, 0, 128);
        setupMotor(R1_RPWM, R1_LPWM, 0, 128);
        setupMotor(R2_RPWM, R2_LPWM, 0, 128);
        // delay(2000);
        break;

      case 'S':  // Stop
        stopAll();
        delay(1000);
        break;
    }

    // Move Reverse
    //  setupMotor(L1_RPWM, L1_LPWM, 0, 128);
    //  setupMotor(L2_RPWM, L2_LPWM, 0, 128);
    //  setupMotor(R1_RPWM, R1_LPWM, 0, 128);
    //  setupMotor(R2_RPWM, R2_LPWM, 0, 128);
    //  delay(2000);

    // Stop
    //  stopAll();
    //  delay(1000);
  }
}
