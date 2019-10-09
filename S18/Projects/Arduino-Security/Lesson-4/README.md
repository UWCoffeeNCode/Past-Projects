# Meet-Up #4 Agenda:

**Objective**: Use at least 1 sensor to make a servo motor move.

## 1. Learning
**What is a servo motor?**

[From Quora: ](https://www.quora.com/What-is-the-difference-between-a-DC-motor-a-servomotor-and-a-stepper-motor)
*Servo  motors are generally an assembly of four things: a DC motor, a gearing  set, a control circuit and a position-sensor (usually a potentiometer).
The  position of servo motors can be controlled more precisely than those of  standard DC motors, and they usually have three wires (power, ground  & control). *

![Servo](https://qph.fs.quoracdn.net/main-qimg-cc92b26486ecf87f1560263b90ead8b7.webp)


**What is PWM?**

[From Wikipedia: ](https://en.wikipedia.org/wiki/Pulse-width_modulation)
*Pulse-width modulation (PWM) is a modulation technique used to encode a message into a pulsing signal. The average value of voltage (and current) fed to the load is controlled by turning the switch between supply and load on and off at a fast rate. The longer the switch is on compared to the off periods, the higher the total power supplied to the load.*

![PWM](https://qph.fs.quoracdn.net/main-qimg-dd4c694c339662aa95ba360e5963f3f0.webp)


## 2. Coding

Pick a sensor, and do some googling around to understand how to read it. Then setup it up to control the servo!

**Servo Code**

Here is an sample Arduino sketch on how to move a servo.
```c++
#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
}

void loop() {
  for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}
```
