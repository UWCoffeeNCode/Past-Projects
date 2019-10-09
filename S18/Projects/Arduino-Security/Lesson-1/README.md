# Meet-Up #1 Agenda:

**Objective**: explain the Arduino security project, learn the basics of Arduino programming, and create list of parts.

## 1. Downloads
* [Arduino IDE](https://www.arduino.cc/en/Main/Software)

* [Arduino Simulator for Web](https://www.tinkercad.com/circuits)
**OR**
[Arduino Simulator for Windows](https://www.sites.google.com/site/unoardusim/services)

## 2. The Security Box Project
* Use an Arduino microcontroller, actuators, and sensors to create a security system to lock a box.
* You will be provided all the tools to build this (including the box).

## 3. Coding
Using the Arduino Simulator create a program that will flash an LED.

*Solution*

```c++
// ensure the LED is connected to pin 7.

// The setup function runs one time only.
void setup()
{
  // initialize digital pin #7 as an output.
  pinMode(7, OUTPUT);
}

// the loop function runs over and over again forever
void loop()
{
  digitalWrite(7, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);                       // wait for a second
  digitalWrite(7, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);                       // wait for a second
}
```

## 4. Optional Homework
* Create a rough sketch of how your security box is going to work.

* Watch [this tutorial video series](https://www.youtube.com/watch?v=09zfRaLEasY&list=PLZfay8jtbyJt6gkkOgeeapCS_UrsgfuJA)
